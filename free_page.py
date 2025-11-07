# free_page.py
import streamlit as st

def show_free_page():
    st.markdown("## 🆓 Free R-score page")
    st.markdown("This is the limited version. Upload a small CSV and get a one-time R-score.")
    st.markdown("_(You can style this like your dashboard later.)_")

    if st.button("Go premium"):
        st.session_state["page"] = "auth"
        st.rerun()

    if st.button("⬅ Back to landing"):
        st.session_state["page"] = "landing"
        st.rerun()
