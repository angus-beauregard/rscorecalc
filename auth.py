# auth.py
import streamlit as st

from supabase import create_client, Client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_ANON_KEY = st.secrets["SUPABASE_ANON_KEY"]

def get_supabase() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

def show_auth():
    st.markdown("## Sign in / Sign up")
    sb = get_supabase()

    tab_login, tab_signup = st.tabs(["Login", "Sign up"])

    # LOGIN
    with tab_login:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            # you can use sb.auth.sign_in_with_password if you enabled auth
            # for now: store email and send to dashboard
            st.session_state["user_email"] = email
            st.session_state["page"] = "dashboard"
            st.rerun()

    # SIGNUP
    with tab_signup:
        email2 = st.text_input("Email", key="signup_email")
        password2 = st.text_input("Password", type="password", key="signup_password")
        if st.button("Create account"):
            st.session_state["user_email"] = email2
            # send to payment page
            st.session_state["page"] = "payment"
            st.rerun()

    if st.button("⬅ Back"):
        st.session_state["page"] = "landing"
        st.rerun()
