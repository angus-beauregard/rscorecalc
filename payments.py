# payments.py
import streamlit as st

def show_payment():
    st.markdown("## Upgrade to Premium")

    user_email = st.session_state.get("user_email")
    if not user_email:
        st.warning("You need to sign in first.")
        if st.button("Go to sign in"):
            st.session_state["page"] = "auth"
            st.rerun()
        return

    # try to import stripe only when needed
    try:
        import stripe
    except Exception:
        st.error("Stripe is not installed. Add `stripe` to requirements.txt.")
        return

    stripe_key = st.secrets.get("STRIPE_SECRET_KEY")
    app_url = st.secrets.get("APP_BASE_URL")
    price_id = st.secrets.get("STRIPE_PRICE_ID")  # we can store it in secrets too

    if not stripe_key or not app_url or not price_id:
        st.error("Stripe secrets missing. Set STRIPE_SECRET_KEY, APP_BASE_URL and STRIPE_PRICE_ID in secrets.")
        return

    stripe.api_key = stripe_key

    st.write("You're about to subscribe to **RScoreCalc Pro** (test).")

    if st.button("Go to Stripe checkout"):
        checkout_session = stripe.checkout.Session.create(
            mode="subscription",
            line_items=[{"price": price_id, "quantity": 1}],
            customer_email=user_email,
            success_url=f"{app_url}?page=success&session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{app_url}?page=payment",
        )
        st.markdown(
            f"<script>window.location.href = '{checkout_session.url}';</script>",
            unsafe_allow_html=True,
        )
