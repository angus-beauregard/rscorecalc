# free_page.py
import streamlit as st
import pandas as pd
import datetime

# Import your r-score math function from dashboard
from dashboard import compute_rscore_school_based, compute_overall_rscore


def show_free_page():
    st.markdown(
        """
        <style>
        :root {
            --rscore-blue: #0f5fff;
        }
        .header {
            font-size: 2rem;
            font-weight: 700;
            color: var(--rscore-blue);
            margin-bottom: 0.2rem;
        }
        .subtitle {
            color: #475569;
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }
        .section {
            margin-top: 1rem;
            margin-bottom: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ---- Header ----
    st.markdown('<div class="header">🎓 Free R-Score Calculator</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Estimate your R-Score using manual entry — instant and simple.</div>',
        unsafe_allow_html=True,
    )

    # ---- Input Section ----
    with st.form("manual_entry_form"):
        c1, c2, c3 = st.columns(3)
        with c1:
            mark = st.number_input("Your mark (%)", 0.0, 100.0, 85.0)
        with c2:
            group_avg = st.number_input("Class average (%)", 0.0, 100.0, 75.0)
        with c3:
            group_sd = st.number_input("Std. deviation", 0.1, 30.0, 8.0)
        submitted = st.form_submit_button("Calculate R-Score")

    if submitted:
        # Basic constants — uses IDGZ=1.0, ISGZ=0.0, same as cegep average baseline
        rscore = compute_rscore_school_based(
            mark, group_avg, group_sd, idgz=1.0, isgz=0.0, C=35.0, D=1.0
        )
        st.success(f"Your estimated **R-Score** is **{rscore}**")

    # ---- Example Explanation ----
    st.markdown(
        """
        <div class="section">
        <h4>📘 How this estimate works</h4>
        <p>
        This free tool uses the standard CEGEP R-Score formula:
        </p>
        <p style="font-family: monospace; background: #f1f5f9; padding: 0.5rem; border-radius: 0.5rem;">
        R = ((Z × IDGZ) + ISGZ + 35) × 1
        </p>
        <p>
        Where Z is your standardized score, based on your mark relative to your class:
        </p>
        <p style="font-family: monospace; background: #f1f5f9; padding: 0.5rem; border-radius: 0.5rem;">
        Z = (Your mark − Class average) ÷ Class standard deviation
        </p>
        <p>
        For this simplified version, we assume:
        <ul>
          <li><strong>IDGZ = 1.0</strong> (average difficulty)</li>
          <li><strong>ISGZ = 0.0</strong> (average strength group)</li>
          <li><strong>C = 35</strong>, <strong>D = 1</strong> (standard constants)</li>
        </ul>
        </p>
        <p>
        The premium version adjusts these based on your real high-school data (IDGZ/ISGZ) for more accuracy and
        lets you upload your full grade list to compute your weighted average automatically.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---- Footer ----
    st.markdown("---")
    st.caption("© rscorecalc.com • This free version uses simplified assumptions for demonstration only.")
