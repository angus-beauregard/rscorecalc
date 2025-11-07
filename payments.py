# payments.py
import streamlit as st
import stripe

def show_payment():
    st.markdown("## Upgrade to Premium")

    user_email = st.session_state.get("user_email")
    if not user_email:
        st.warning("You need to sign in first.")
        if st.button("Go to sign in"):
            st.session_state["page"] = "auth"
            st.rerun()
        return

    stripe.api_key = st.secrets["STRIPE_SECRET_KEY"]
    base_url = st.secrets["APP_BASE_URL"]

    st.write("You're about to subscribe to **RScoreCalc Pro** (test mode).")

    if st.button("Go to Stripe checkout"):
        # create checkout session
        checkout_session = stripe.checkout.Session.create(
            mode="subscription",   # or "payment" if one-time
            line_items=[
                {
                    "price": "price_1SQqvSHm1An0Oa2hLoDpgaZw",  # <-- put your Stripe PRICE ID here
                    "quantity": 1,
                }
            ],
            customer_email=user_email,
            success_url=f"{base_url}?page=success&session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{base_url}?page=payment",
        )

        # redirect with javascript
        st.markdown(
            f"""
            <script>
            window.location.href = "{checkout_session.url}";
            </script>
            """,
            unsafe_allow_html=True,
        )
    st.info("Use Stripe test card 4242 4242 4242 4242 to test.")

