import datetime
import os
import pandas as pd
import streamlit as st

# ---------------------------------------------------------
# OCR fallback
# ---------------------------------------------------------
try:
    from ocr_engine import extract_courses_from_image
except Exception:
    def extract_courses_from_image(_bytes):
        return pd.DataFrame(
            columns=["course_name", "mark", "group_avg", "group_sd", "credits"]
        )

# ---------------------------------------------------------
# Load IDGZ / ISGZ table
# ---------------------------------------------------------
IDGZ_CSV_PATH = "idgz+isgz_data.csv"

def load_idgz_table(path=IDGZ_CSV_PATH):
    if not os.path.exists(path):
        return pd.DataFrame({"school": ["(default)"], "isgz": [0.0], "idgz": [1.0]})

    df = pd.read_csv(path)
    df = df.rename(columns={c: c.strip().lower() for c in df.columns})

    def pick(cols):
        for c in cols:
            if c in df.columns:
                return c
        return None

    school_col = pick(["school board", "school", "high school", "board", "school name"])
    isgz_col = pick(["isgz estimate", "isgz", "isg"])
    idgz_col = pick(["idgz estimate", "idgz", "idg"])

    return pd.DataFrame({
        "school": df[school_col] if school_col else ["(default)"],
        "isgz": df[isgz_col] if isgz_col else 0.0,
        "idgz": df[idgz_col] if idgz_col else 1.0,
    })

hs_df = load_idgz_table()

# ---------------------------------------------------------
# R-score math
# ---------------------------------------------------------
def compute_rscore_school_based(mark, group_avg, group_sd, idgz=1.0, isgz=0.0, C=35.0, D=1.0):
    if group_sd is None or group_sd == 0:
        z = 0
    else:
        z = (mark - group_avg) / group_sd
    return round((z * idgz + isgz + C) * D, 2)

def compute_overall_rscore(df):
    if df.empty:
        return 0.0
    df = df.copy()
    if "credits" not in df.columns:
        df["credits"] = 1
    weighted = (df["rscore"] * df["credits"]).sum()
    total = df["credits"].sum()
    return round(weighted / total, 2) if total else 0.0

# ---------------------------------------------------------
# Supabase (lazy load)
# ---------------------------------------------------------
from supabase import create_client

def get_supabase():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise Exception("Supabase credentials missing")
    return create_client(url, key)

def save_rscore_to_db(user_email, rscore):
    try:
        supabase = get_supabase()
        supabase.table("user_rscores").upsert(
            {"email": user_email, "rscore": rscore, "timestamp": datetime.datetime.now().isoformat()}
        ).execute()
    except Exception:
        pass

# ---------------------------------------------------------
# CSV cleaning
# ---------------------------------------------------------
def normalize_col_name(raw):
    s = raw.strip().lower()
    s = s.replace(".", " ").replace("_", " ").replace("-", " ")
    s = " ".join(s.split())
    if "course" in s:
        return "course_name"
    if any(x in s for x in ["grade", "mark", "score"]):
        return "mark"
    if "avg" in s:
        return "group_avg"
    if "sd" in s or "std" in s:
        return "group_sd"
    if "credit" in s:
        return "credits"
    return s

def coerce_csv_columns(df):
    df = df.rename(columns={c: normalize_col_name(c) for c in df.columns})
    needed = ["course_name", "mark", "group_avg", "group_sd", "credits"]
    for col in needed:
        if col not in df.columns:
            if col == "credits":
                df["credits"] = 1
            else:
                raise ValueError(f"Missing {col} column.")
    return df[needed]

# ---------------------------------------------------------
# MAIN DASHBOARD PAGE
# ---------------------------------------------------------
def show_dashboard():

    # Initialize state
    if "courses" not in st.session_state:
        st.session_state["courses"] = pd.DataFrame(
            columns=["course_name", "mark", "group_avg", "group_sd", "credits"]
        )
    if "target_r" not in st.session_state:
        st.session_state["target_r"] = 32.0
    if "semester_start" not in st.session_state:
        st.session_state["semester_start"] = datetime.date(2025, 8, 26)
    if "semester_end" not in st.session_state:
        st.session_state["semester_end"] = datetime.date(2025, 12, 19)

    st.title("📊 RScore Premium Dashboard")
    st.write("Upload your grades, apply school factors, and compute your R-score.")

    # 2-column layout
    col1, col2 = st.columns([1, 2], gap="large")

    # ---------------------------------------------------------
    # LEFT PANEL
    # ---------------------------------------------------------
    with col1:

        st.markdown("### 🏫 School Selector")
        school = st.selectbox(
            "Choose your school",
            hs_df["school"].tolist(),
            index=0
        )

        # School factors
        hs_row = hs_df[hs_df["school"] == school].iloc[0]
        idgz_val = float(hs_row["idgz"])
        isgz_val = float(hs_row["isgz"])

        st.markdown("### 🎯 R-Score Overview")
        df_current = st.session_state["courses"].copy()

        if not df_current.empty:
            df_current["rscore"] = df_current.apply(
                lambda r: compute_rscore_school_based(
                    r["mark"], r["group_avg"], r["group_sd"],
                    idgz=idgz_val, isgz=isgz_val
                ),
                axis=1
            )
            final = compute_overall_rscore(df_current)
            st.metric("Final R-Score", final)
            st.session_state["final_rscore"] = final
        else:
            st.metric("Final R-Score", "—")

        st.markdown("### ⏳ Semester Countdown")
        today = datetime.date.today()
        remaining = (st.session_state["semester_end"] - today).days

        if remaining >= 0:
            st.write(f"📅 {remaining} days remaining")
        else:
            st.write("📅 Semester completed 🎉")

    # ---------------------------------------------------------
    # RIGHT PANEL (TABS)
    # ---------------------------------------------------------
    with col2:

        tabs = st.tabs([
            "📸 OCR Upload",
            "📄 CSV Upload",
            "✏️ Manual Entry",
            "📈 Biggest Gains",
            "🎯 Goals"
        ])

        # -----------------------------------------------------
        # TAB 1: OCR Upload
        # -----------------------------------------------------
        with tabs[0]:
            st.markdown("#### OCR Upload (photo-to-table)")
            img = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])
            if img:
                df_ocr = extract_courses_from_image(img.read())
                st.write("Extracted data:")
                st.dataframe(df_ocr)
                st.session_state["courses"] = pd.concat(
                    [st.session_state["courses"], df_ocr], ignore_index=True
                )

        # -----------------------------------------------------
        # TAB 2: CSV Upload
        # -----------------------------------------------------
        with tabs[1]:
            st.markdown("#### Upload CSV")
            f = st.file_uploader("Upload CSV", type=["csv"])
            if f:
                try:
                    df_csv = pd.read_csv(f)
                    df_csv = coerce_csv_columns(df_csv)
                    st.session_state["courses"] = df_csv
                except Exception as e:
                    st.error(f"CSV error: {e}")

            st.dataframe(st.session_state["courses"], use_container_width=True)

        # -----------------------------------------------------
        # TAB 3: Manual Entry
        # -----------------------------------------------------
        with tabs[2]:
            st.markdown("#### Add a Course")
            with st.form("manual"):
                cname = st.text_input("Course name")
                mark = st.number_input("Mark (%)", 0, 100, 85)
                gavg = st.number_input("Group Avg (%)", 0, 100, 75)
                gsd = st.number_input("Std Dev", 0.1, 30.0, 8.0)
                creds = st.number_input("Credits", 0.5, 8.0, 2.0)
                ok = st.form_submit_button("Add")
            if ok:
                st.session_state["courses"] = pd.concat([
                    st.session_state["courses"],
                    pd.DataFrame([{
                        "course_name": cname,
                        "mark": mark,
                        "group_avg": gavg,
                        "group_sd": gsd,
                        "credits": creds
                    }])
                ], ignore_index=True)

        # -----------------------------------------------------
        # TAB 4: Biggest Gains
        # -----------------------------------------------------
        with tabs[3]:
            st.markdown("#### Biggest R-Score Gains")
            if st.session_state["courses"].empty:
                st.info("Upload or add courses first.")
            else:
                bump = st.number_input("Simulate +X to each mark:", 1, 15, 5)

                df2 = st.session_state["courses"].copy()
                df2["rscore"] = df2.apply(
                    lambda r: compute_rscore_school_based(
                        r["mark"], r["group_avg"], r["group_sd"],
                        idgz=idgz_val, isgz=isgz_val
                    ),
                    axis=1
                )

                base = compute_overall_rscore(df2)
                rows = []
                for i, row in df2.iterrows():
                    temp = df2.copy()
                    temp.loc[i, "rscore"] = compute_rscore_school_based(
                        min(row["mark"] + bump, 100), row["group_avg"], row["group_sd"],
                        idgz=idgz_val, isgz=isgz_val
                    )
                    new = compute_overall_rscore(temp)
                    rows.append({
                        "course_name": row["course_name"],
                        "current_mark": row["mark"],
                        f"gain_if_+{bump}": round(new - base, 3)
                    })
                out = pd.DataFrame(rows).sort_values(f"gain_if_+{bump}", ascending=False)
                st.dataframe(out, use_container_width=True)

        # -----------------------------------------------------
        # TAB 5: Goals
        # -----------------------------------------------------
        with tabs[4]:
            st.markdown("#### Set Your Target R-score")
            st.session_state["target_r"] = st.number_input(
                "Target:", 0.0, 50.0, st.session_state["target_r"], 0.1
            )
            st.success("Target updated!")

