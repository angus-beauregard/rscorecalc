# landing.py
import streamlit as st

def show_landing():
    # ===== blue theme styling =====
    st.markdown(
        """
        <style>
        :root {
            --rscore-blue: #0f5fff;
            --rscore-blue-soft: rgba(15, 95, 255, 0.08);
        }
        .hero-title {
            font-size: 2.6rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
            color: #0f172a;
        }
        .hero-subtitle {
            font-size: 1.05rem;
            color: #334155;
            margin-bottom: 1.5rem;
        }
        .pill {
            background: var(--rscore-blue-soft);
            color: var(--rscore-blue);
            display: inline-block;
            padding: 0.35rem 0.8rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            margin-bottom: 0.75rem;
        }
        .card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 1rem;
            padding: 1rem 1.1rem;
            height: 100%;
        }
        .section-title {
            font-size: 1.4rem;
            font-weight: 600;
            margin-top: 2.5rem;
            margin-bottom: 0.75rem;
            color: #0f172a;
        }
        .pricing-table {
            border: 1px solid #e2e8f0;
            border-radius: 1rem;
            background: white;
        }
        .pricing-header {
            background: #eff6ff;
            padding: 0.6rem 1rem;
            border-radius: 1rem 1rem 0 0;
            font-weight: 600;
            color: #0f172a;
        }
        .pricing-row {
            display: flex;
            justify-content: space-between;
            padding: 0.4rem 1rem;
            border-bottom: 1px solid #e2e8f0;
            font-size: 0.9rem;
        }
        .pricing-row:last-child {
            border-bottom: none;
        }
        .logo-text {
            font-weight: 700;
            color: #0f172a;
            font-size: 1.15rem;
        }
        .footer {
            font-size: 0.78rem;
            color: #475569;
            margin-top: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .tos-link {
            color: #0f5fff;
            text-decoration: underline;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ===== header =====
    st.markdown('<span class="logo-text">rscorecalc.com</span>', unsafe_allow_html=True)
    st.markdown('<div class="pill">Built for Québec / CEGEP students</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Remove the mystery around your R-score.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">RScoreCalc gives you instant R-score updates, shows you the biggest grade gains, and maps you to your program.</div>',
        unsafe_allow_html=True,
    )

    # ===== main buttons =====
    c1, c2 = st.columns([0.5, 0.5])
    with c1:
        if st.button("🚀 Try free calculator", use_container_width=True):
            st.session_state["page"] = "free"
            st.rerun()
    with c2:
        if st.button("🔒 Go premium", use_container_width=True, type="primary"):
            st.session_state["page"] = "auth"
            st.rerun()
    st.markdown("No credit card for free plan • Seconds to upload • Made for rscorecalc.com")

    # ===== "What you get" section under buttons =====
    st.markdown('<div class="section-title">What you get</div>', unsafe_allow_html=True)
    st.markdown("""
    - ✅ R-score calculator based on your Excel logic  
    - 📊 Biggest gains tool  
    - 🎯 Goals + semester countdown  
    - 💳 Stripe-ready premium upgrade  
    """)

    # ===== free vs premium =====
    st.markdown('<div class="section-title">Free vs. Premium</div>', unsafe_allow_html=True)
    col_free, col_premium = st.columns(2)
    with col_free:
        st.markdown('<div class="pricing-table">', unsafe_allow_html=True)
        st.markdown('<div class="pricing-header">Free</div>', unsafe_allow_html=True)
        st.markdown('<div class="pricing-row"><span>Upload CSV manually</span><span>✔</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="pricing-row"><span>One dashboard session</span><span>✔</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="pricing-row"><span>OCR uploads</span><span>—</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="pricing-row"><span>Biggest gains ranking</span><span>—</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="pricing-row"><span>Goals + countdown</span><span>—</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_premium:
        st.markdown('<div class="pricing-table">', unsafe_allow_html=True)
        st.markdown('<div class="pricing-header" style="background:#0f5fff;color:white;">Premium</div>', unsafe_allow_html=True)
        st.markdown('<div class="pricing-row"><span>OCR + CSV + manual</span><span>✔</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="pricing-row"><span>Unlimited sessions</span><span>✔</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="pricing-row"><span>Biggest gains tab</span><span>✔</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="pricing-row"><span>Goals + target R</span><span>✔</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="pricing-row"><span>Stripe subscription</span><span>✔</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ===== email list =====
    st.markdown('<div class="section-title">Join the list</div>', unsafe_allow_html=True)
    st.markdown("Get notified when we add real college averages + mobile app.")
    with st.form("email_capture"):
        email = st.text_input("Email", placeholder="you@example.com")
        submitted = st.form_submit_button("Join the list")
    if submitted and email:
        st.success("You're on the list ✅")

    # ===== footer =====
    st.markdown(
        """
        <div class="footer">
            <div>© rscorecalc.com</div>
            <div class="tos-link" onclick="window.parent.postMessage({ type: 'page', page: 'tos' }, '*')">Terms of Service</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # workaround for navigation in Streamlit
    st.markdown(
        """
        <script>
        window.addEventListener('message', (event) => {
            if (event.data.type === 'page' && event.data.page === 'tos') {
                window.parent.postMessage({streamlitRerun: {page: 'tos'}}, '*');
            }
        });
        </script>
        """,
        unsafe_allow_html=True,
    )

    # Streamlit-compatible redirect
    if "_REACTPY" in st.session_state:
        del st.session_state["_REACTPY"]
