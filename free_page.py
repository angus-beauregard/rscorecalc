# free_page.py
import streamlit as st
import pandas as pd
from dashboard import compute_rscore_school_based, compute_overall_rscore

def show_free_page():
    # ---- Styling ----
    st.markdown("""
        <style>
        :root {
            --rscore-blue: #0f5fff;
            --rscore-bg-light: #f8fafc;
            --rscore-bg-dark: #1e293b;
            --rscore-text-light: #0f172a;
            --rscore-text-dark: #f1f5f9;
        }
        .header {
            font-size: 2rem;
            font-weight: 700;
            color: var(--rscore-blue);
            margin-bottom: 0.25rem;
        }
        .subtitle {
            font-size: 1rem;
            color: var(--rscore-text-light);
            margin-bottom: 1.5rem;
        }
        @media (prefers-color-scheme: dark) {
            .subtitle { color: var(--rscore-text-dark); }
        }
        .section {
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        .explanation-box {
            background: var(--rscore-bg-light);
            border-radius: 1rem;
            padding: 1rem 1.25rem;
            margin-top: 1rem;
            color: var(--rscore-text-light);
        }
        @media (prefers-color-scheme: dark) {
            .explanation-box { background: var(--rscore-bg-dark); color: var(--rscore-text-dark); }
        }
        </style>
    """, unsafe_allow_html=True)

    # ---- Header ----
    st.markdown('<div class="header">🎓 Free R-Score Calculator</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Estimate your R-Score using manual entry — simple, fast, and accurate.</div>',
        unsafe_allow_html=True,
    )

    # ---- Data Entry ----
    st.markdown("### Add your courses below")
    st.caption("Enter your course name, grade, group average, standard deviation, and credits.")

    if "free_courses" not in st.session_state:
        st.session_state["free_courses"] = pd.DataFrame(
            columns=["Course", "Grade", "Group Avg", "Std. Dev", "Credits"]
        )

    with st.form("manual_form"):
        c1, c2, c3, c4, c5 = st.columns(5)
        with c1:
            cname = st.text_input("Course")
        with c2:
            mark = st.number_input("Grade (%)", 0.0, 100.0, 85.0)
        with c3:
            gavg = st.number_input("Group Avg (%)", 0.0, 100.0, 75.0)
        with c4:
            gsd = st.number_input("Std. Dev", 0.1, 30.0, 8.0)
        with c5:
            creds = st.number_input("Credits", 0.5, 10.0, 2.0)
        submitted = st.form_submit_button("Add Course")

    if submitted:
        new_row = {"Course": cname, "Grade": mark, "Group Avg": gavg, "Std. Dev": gsd, "Credits": creds}
        st.session_state["free_courses"] = pd.concat(
            [st.session_state["free_courses"], pd.DataFrame([new_row])],
            ignore_index=True,
        )
        st.success(f"Added {cname}")

    # ---- Display Courses ----
    df = st.session_state["free_courses"]
    if not df.empty:
        # Compute R-Scores for each course
        df["R-Score"] = df.apply(
            lambda row: compute_rscore_school_based(
                row["Grade"], row["Group Avg"], row["Std. Dev"], idgz=1.0, isgz=0.0
            ),
            axis=1,
        )
        overall = compute_overall_rscore(
            df.rename(columns={
                "Course": "course_name",
                "Grade": "mark",
                "Group Avg": "group_avg",
                "Std. Dev": "group_sd",
                "Credits": "credits",
                "R-Score": "rscore"
            })
        )

        st.markdown("### Your Courses")
        st.dataframe(df, hide_index=True, use_container_width=True)

        st.markdown(f"### 🧮 Estimated Overall R-Score: **{overall}**")

    else:
        st.info("Add at least one course to calculate your R-Score.")

    # ---- Explanation Section ----
    st.markdown('<div class="section"><h4>📘 How it Works</h4></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="explanation-box">
        <p><strong>R-Score Formula:</strong></p>
        <p style="font-family: monospace;">R = ((Z × IDGZ) + ISGZ + 35) × 1</p>
        <p>
        Where <strong>Z</strong> is your standardized score compared to your class:
        </p>
        <p style="font-family: monospace;">Z = (Your Grade − Class Average) ÷ Class Std. Dev</p>

        <p><strong>In this free version:</strong></p>
        <ul>
            <li>IDGZ (difficulty) = 1.0</li>
            <li>ISGZ (strength group) = 0.0</li>
            <li>C = 35, D = 1 — standard constants</li>
        </ul>

        <p>
        Each course has its own R-Score, and your <strong>final R-Score</strong> is a 
        <strong>credit-weighted average</strong> of all your course R-Scores:
        </p>

        <p style="font-family: monospace;">Overall R = Σ(R_course × Credits) ÷ Σ(Credits)</p>

        <p>
        This weighting means that higher-credit courses have a greater impact on your overall R-Score.
        </p>

        <p>
        <em>The Premium version</em> adjusts for your real school difficulty (IDGZ) and cohort strength (ISGZ),
        and supports CSV/OCR uploads for instant updates across all your classes.
        </p>
        </div>
    """, unsafe_allow_html=True)

    # ---- Footer ----
    st.markdown("---")
    st.caption("© rscorecalc.com • Free version uses simplified constants (IDGZ=1.0, ISGZ=0.0).")
