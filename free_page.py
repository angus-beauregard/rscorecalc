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
            gsd =
