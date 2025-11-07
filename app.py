# app.py
import streamlit as st

from landing import show_landing
from free_page import show_free_page
from auth import show_auth
from dashboard import show_dashboard
from payments import show_payment
from tos import show_tos  # <— we'll make this

st.set_page_config(page_title="RScoreCalc", layout="wide", page_icon="📈")

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
elif page == "tos":
    show_tos()
else:
    show_landing()
