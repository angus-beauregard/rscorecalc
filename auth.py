# auth.py
import streamlit as st

SUPABASE_URL = "https://ezaddmknwhtzintwxwew.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV6YWRkbWtud2h0emludHd4d2V3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjIyNzIwNzcsImV4cCI6MjA3Nzg0ODA3N30.DQILlLtDtVBVx3abeUnud1vzdIKSgMS-6zEEF_M6dqQ"

def get_supabase():
    try:
        from supabase import create_client
        return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)
    except Exception:
        return None

def show_auth():
    st.markdown("## Sign in / Sign up")
    st.markdown("Use your email to access the premium dashboard.")

    sb = get_supabase()
    if sb is None:
        st.warning("Supabase client not installed. `pip install supabase` (or `supabase-py`) to enable real auth.")

    tab_login, tab_signup = st.tabs(["Login", "Sign up"])

    # LOGIN
    with tab_login:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            if sb:
                # real Supabase call
                res = sb.auth.sign_in_with_password({"email": email, "password": password})
                if res.user:
                    st.session_state["is_premium"] = True  # or check a table
                    st.session_state["page"] = "dashboard"
                    st.rerun()
                else:
                    st.error("Login failed.")
            else:
                # fallback for local testing
                st.session_state["is_premium"] = False
                st.session_state["page"] = "dashboard"
                st.rerun()

    # SIGNUP
    with tab_signup:
        email2 = st.text_input("Email", key="signup_email")
        password2 = st.text_input("Password", type="password", key="signup_password")
        if st.button("Create account"):
            if sb:
                res = sb.auth.sign_up({"email": email2, "password": password2})
                if res.user:
                    # after signup, send them to pay
                    st.session_state["pending_email"] = email2
                    st.session_state["page"] = "payment"
                    st.rerun()
                else:
                    st.error("Could not create account.")
            else:
                st.session_state["pending_email"] = email2
                st.session_state["page"] = "payment"
                st.rerun()

    if st.button("⬅ Back"):
        st.session_state["page"] = "landing"
        st.rerun()
