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
        .about-card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 1rem;
            padding: 1rem 1.1rem;
            line-height: 1.6;
        }
        code {
            background: #f1f5f9;
            padding: 0.15rem 0.35rem;
            border-radius: 0.3rem;
            font-size: 0.85rem;
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
    st.markdown(
        """
    - ✅ R-score calculator tied to your real grades  
    - 📊 “Biggest gains” tool showing what class raises your R the most  
    - 🎯 Goal tracker + semester countdown  
    - 💳 Stripe-ready premium upgrade  
    """
    )

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

    # ===== ABOUT SECTION =====
    st.markdown(
        """
        <div class="section-title">How your R-score is calculated</div>
        <div class="about-card">
            <p><b>Your R-score reflects both your individual performance and the academic strength of your peers and school.</b></p>

            <p>Each of your courses produces its own <i>individual R-score</i> using the official Québec CÉGEP formula:</p>

            <p style="font-size:1.05rem; margin:0.5rem 0;"><b>R = ((Z × IDGZ) + ISGZ + C) × D</b></p>

            <p>Here’s how it works:</p>
            <ul>
                <li><b>Z</b> — Measures how far your grade is from the class average. It accounts for how spread out everyone’s results are (the standard deviation).</li>
                <li><b>IDGZ</b> — Reflects how strong your class group is academically compared to others.</li>
                <li><b>ISGZ</b> — Reflects the overall strength of your high school or school board.</li>
                <li><b>C</b> and <b>D</b> — Constants used to align scores with Québec’s official range (we use C ≈ 35 and D = 1).</li>
            </ul>

            <p>Once every course’s R-score is calculated, we combine them into your <b>final or semester R-score</b> using course credits to weight each one:</p>

            <p style="font-size:1.05rem; margin:0.5rem 0;"><b>Final R = (Σ (R<sub>course</sub> × credits)) ÷ (Σ credits)</b></p>

            <p>That means high-credit courses — like Chemistry or Calculus — have a bigger impact on your overall R-score than smaller ones like labs or tutorials.</p>

            <p>RScoreCalc does all of this automatically when you upload your CSV or use OCR. It instantly reads your grades, averages, and deviations, applies your school’s IDGZ and ISGZ values, and produces your personalized R-score breakdown — no manual math needed.</p>

            <p style="font-size:0.85rem; color:#475569; margin-top:1rem;">
            <i>Based on public documentation from the Ministère de l’Enseignement supérieur and official CÉGEP R-score methodology, adapted for transparency through RScoreCalc.</i>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ===== email list =====
    st.markdown('<div class="section-title">Join the list</div>', unsafe_allow_html=True)
    st.markdown("Get notified when we add real college averages + mobile app.")
    with st.form("email_capture"):
        email = st.text_input("Email", placeholder="you@example.com")
        submitted = st.form_submit_button("Join the list")
    if submitted and email:
        st.success("You're on the list ✅")

    # ===== footer =====
    footer_left, footer_right = st.columns([0.5, 0.5])
    with footer_left:
        st.markdown("© rscorecalc.com")
    with footer_right:
        if st.button("Terms of service", help="View terms for rscorecalc.com"):
            st.session_state["page"] = "tos"
            st.rerun()


