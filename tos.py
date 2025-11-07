# tos.py
import streamlit as st

def show_tos():
    st.markdown("## Terms of Service")
    st.write("Last updated: today.")
    st.write(
        """
        This tool is an R-score helper for Québec students. We do not guarantee admission decisions.
        Your data stays in your browser unless you choose to save it.
        Payments are handled by Stripe.
        """
    )
    if st.button("Back to landing"):
        st.session_state["page"] = "landing"
        st.rerun()
