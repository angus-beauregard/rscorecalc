# auth.py
import streamlit as st

SUPABASE_URL = st.secrets.get("SUPABASE_URL")
SUPABASE_ANON_KEY = st.secrets.get("SUPABASE_ANON_KEY")

def get_supabase():
    """Try to create a Supabase client, but don't crash the app if package is missing."""
    if not SUPABASE_URL or not SUPABASE_ANON_KEY:
        return None
    try:
        from supabase import create_client
        return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
    except Exception:
        return None

def show_auth():
    st.markdown("## Sign in / Sign up")

    sb = get_supabase()
    if sb is None:
        st.info("Supabase not available right now. We will still let you continue for testing.")

    tab_login, tab_signup = st.tabs(["Login", "Sign up"])

    # LOGIN
    with tab_login:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            # if Supabase worked, you would check credentials here
            st.session_state["user_email"] = email
            st.session_state["page"] = "dashboard"
            st.rerun()

    # SIGNUP
    with tab_signup:
        email2 = st.text_input("Email", key="signup_email")
        password2 = st.text_input("Password", type="password", key="signup_password")
        if st.button("Create account"):
            st.session_state["user_email"] = email2
            # send to payment, even if Supabase isn't set up yet
            st.session_state["page"] = "payment"
            st.rerun()

    if st.button("⬅ Back"):
        st.session_state["page"] = "landing"
        st.rerun()
