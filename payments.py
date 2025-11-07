# payments.py
import streamlit as st

STRIPE_CHECKOUT_URL = "https://buy.stripe.com/9B68wPcz4d4bbNgc9id7q00"

def show_payment():
    st.markdown("## Upgrade to Premium")
    st.markdown("You're almost there. Complete your payment to unlock the full RScore dashboard.")
    st.link_button("Go to secure Stripe checkout", STRIPE_CHECKOUT_URL)

    st.markdown("After payment, you can mark the user as premium in Supabase (table: `users`, column: `is_premium = true`).")

    if st.button("⬅ Back"):
        st.session_state["page"] = "landing"
        st.rerun()
