# success.py
import streamlit as st

def show_success():
    """
    Displayed after successful Stripe checkout.
    Redirects user to dashboard and grants premium access.
    """

    st.set_page_config(page_title="Success | RScoreCalc", layout="centered", page_icon="✅")

    st.markdown("## 🎉 Payment Successful!")
    st.write("Thank you for subscribing to **RScoreCalc Pro**.")
    st.success("Your payment has been confirmed and premium access is now active.")

    # Update user session (grant premium access)
    st.session_state["premium_user"] = True

    # Optional success message
    st.markdown("---")
    st.info("You can now access all premium features including:")
    st.markdown("""
    - 📊 Advanced R-score analytics  
    - 🔍 OCR + CSV uploads  
    - 🧮 Goals and countdown tracker  
    - 💎 Unlimited dashboard sessions  
    """)

    # Navigation buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Go to Dashboard"):
            st.session_state["page"] = "dashboard"
            st.rerun()
    with col2:
        if st.button("Back to Landing Page"):
            st.session_state["page"] = "landing"
            st.rerun()
