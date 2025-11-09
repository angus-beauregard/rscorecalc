import streamlit as st
import streamlit.components.v1 as components

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

    # ===== HEADER =====
    st.markdown('<span class="logo-text">rscorecalc.com</span>', unsafe_allow_html=True)
    st.markdown('<div class="pill">Built for Québec / CEGEP students</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Remove the mystery around your R-score.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">RScoreCalc gives you instant R-score updates, shows you the biggest grade gains, and maps you to your program.</div>',
        unsafe_allow_html=True,
    )

    # ===== MAIN BUTTONS =====
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

    # ===== WHAT YOU GET =====
    st.markdown('<div class="section-title">What you get</div>', unsafe_allow_html=True)
    st.markdown("""
    - ✅ R-score calculator based on your Excel logic  
    - 📊 Biggest gains tool  
    - 🎯 Goals + semester countdown  
    - 💳 Stripe-ready premium upgrade  
    """)

    # ===== FREE VS PREMIUM =====
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

    # ===== ABOUT SECTION (FULL HTML) =====
    components.html(
        """
        <div style="font-family: 'Inter', sans-serif; max-width: 900px; margin: auto;">
            <h3 style="color:#0f172a; font-size:1.4rem; font-weight:600;">How your R-score is calculated</h3>
            <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:1rem; padding:1.3rem 1.5rem; line-height:1.6;">
                <p><b>Your R-score reflects both your performance and the academic strength of your peers and school.</b></p>

                <p>Each of your courses has its own <i>individual R-score</i>, calculated using the same structure used by Québec CÉGEPs:</p>

                <p style="font-size:1.1rem; margin:0.5rem 0;"><b>R = ((Z × IDGZ) + ISGZ + C) × D</b></p>

                <p>Here’s what that means:</p>
                <ul style="margin-left:1rem;">
                    <li><b>Z</b> — Measures how far your grade is from the class average, adjusted by the class’s standard deviation.</li>
                    <li><b>IDGZ</b> — Reflects how strong your specific class group is academically.</li>
                    <li><b>ISGZ</b> — Represents the overall strength of your high school or school board.</li>
                    <li><b>C</b> and <b>D</b> — Constants used to keep R-scores within the official Québec range (we use C ≈ 35, D = 1).</li>
                </ul>

                <p>Once each course’s R-score is calculated, we combine them into your <b>final or semester R-score</b> using the credit weight of each course:</p>

                <p style="font-size:1.1rem; margin:0.5rem 0;"><b>Final R = (Σ (R<sub>course</sub> × credits)) ÷ (Σ credits)</b></p>

                <p>That means high-credit courses (like Chemistry or Calculus) have a larger impact on your overall R-score than smaller ones.</p>

                <p>RScoreCalc does all of this automatically: when you upload your grades, it reads your averages and deviations, applies your school’s IDGZ and ISGZ values, and calculates your personalized R-score instantly.</p>

                <p style="font-size:0.85rem; color:#475569; margin-top:1rem;">
                    <i>Based on official documentation from the Ministère de l’Enseignement supérieur and standard CÉGEP R-score methodology, adapted for transparency through RScoreCalc.</i>
                </p>
            </div>
        </div>
        """,
        height=600,
    )

    # ===== EMAIL LIST =====
    st.markdown('<div class="section-title">Join the list</div>', unsafe_allow_html=True)
    st.markdown("Get notified when we add real college averages + mobile app.")
    with st.form("email_capture"):
        email = st.text_input("Email", placeholder="you@example.com")
        submitted = st.form_submit_button("Join the list")
    if submitted and email:
        st.success("You're on the list ✅")

    # ===== FOOTER =====
    st.markdown(
        """
        <div class="footer">
            <div>© rscorecalc.com</div>
            <div class="tos-link" onclick="window.parent.postMessage({ type: 'page', page: 'tos' }, '*')">Terms of Service</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
