# app.py
import streamlit as st
import datetime

from landing import show_landing
from free_page import show_free_page
from auth import show_auth
from dashboard import show_dashboard
from payments import show_payment
from success import show_success
from tos import show_tos

st.set_page_config(
    page_title="RScoreCalc",
    layout="wide",
    page_icon="📈"
)

# ---------------------------------------------------------
# SIDEBAR COMPONENTS
# ---------------------------------------------------------

def show_school_selector():
    st.subheader("🏫 School")
    return st.selectbox(
        "Select your school",
        [
            "John Abbott College",
            "Marianopolis College",
            "Vanier College",
            "Dawson College",
            "Champlain College",
            "Heritage College",
            "Ahuntsic College",
        ],
        index=0
    )

def show_rscore_overview():
    st.markdown("### 🎯 R-Score Overview")

    # Only show real values if they exist
    if "final_rscore" in st.session_state:
        st.metric("Final R-Score", st.session_state["final_rscore"])
    else:
        st.metric("Final R-Score", "—")

def show_semester_countdown():
    st.markdown("### ⏳ Semester Countdown")
    semester_end = datetime.date(2025, 12, 20)
    today = datetime.date.today()
    remaining = (semester_end - today).days

    if remaining >= 0:
        st.write(f"{remaining} days remaining")
    else:
        st.write("Semester completed 🎉")

# ---------------------------------------------------------
# RENDER SIDEBAR (Always Visible)
# ---------------------------------------------------------

with st.sidebar:
    st.title("📘 RScoreCalc")

    # Navigation buttons
    if st.button("🏠 Home"):
        st.session_state["page"] = "landing"
    if st.button("🆓 Free Tool"):
        st.session_state["page"] = "free"
    if st.button("📊 Dashboard"):
        st.session_state["page"] = "dashboard"
    if st.button("💳 Premium"):
        st.session_state["page"] = "payment"

    st.divider()

    # Sidebar widgets
    selected_school = show_school_selector()
    show_rscore_overview()
    show_semester_countdown()

# ---------------------------------------------------------
# PAGE ROUTING
# ---------------------------------------------------------

if "page" not in st.session_state:
    st.session_state["page"] = "landing"

page = st.session_state["page"]

if page == "landing":
    show_landing()
elif page == "free":
    show_free_page()
elif page == "auth":
    show_auth()
elif page == "dashboard":
    show_dashboard()
elif page == "payment":
    show_payment()
elif page == "success":
    show_success()
elif page == "tos":
    show_tos()
else:
    show_landing()
