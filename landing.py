import streamlit as st
import streamlit.components.v1 as components

def show_landing():
    # ===== blue + dark theme CSS =====
    st.markdown("""
        <style>
        :root {
            --rscore-blue: #0f5fff;
            --rscore-blue-soft: rgba(15, 95, 255, 0.08);
            --bg-light: #ffffff;
            --bg-dark: #0f172a;
            --text-light: #0f172a;
            --text-dark: #e2e8f0;
            --subtext-light: #334155;
            --subtext-dark: #94a3b8;
        }

        body { transition: background 0.3s ease, color 0.3s ease; }

        @media (prefers-color-scheme: dark) {
            html, body, .block-container {
                background-color: var(--bg-dark);
                color: var(--text-dark);
            }
        }

        @media (prefers-color-scheme: light) {
            html, body, .block-container {
                background-color: var(--bg-light);
                color: var(--text-light);
            }
        }

        .hero-title {
            font-size: 2.6rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }
        @media (prefers-color-scheme: dark) {
            .hero-title {
                color: #ffffff;
                text-shadow: 0 0 10px rgba(15,95,255,0.25);
            }
        }

        .hero-subtitle {
            font-size: 1.05rem;
            margin-bottom: 1.5rem;
            transition: color 0.3s ease;
        }

        @media (prefers-color-scheme: light) {
            .hero-subtitle {
                color: #334155;  /* dark gray for light mode */
            }
        }

        @media (prefers-color-scheme: dark) {
            .hero-subtitle {
                color: #ffffff;  /* bright white for dark mode */
            }
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
        }
        .footer {
            font-size: 0.78rem;
            margin-top: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .tos-link {
            color: var(--rscore-blue);
            text-decoration: underline;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    # ===== header =====
    st.markdown('<span style="font-weight:700;">rscorecalc.com</span>', unsafe_allow_html=True)
    st.markdown('<div class="pill">Built for Québec / CEGEP students</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">Remove the mystery around your R-score.</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">RScoreCalc gives you instant R-score updates, shows you the biggest grade gains, and maps you to your program.</div>', unsafe_allow_html=True)

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

    # ===== What you get =====
    st.markdown('<div class="section-title">What you get</div>', unsafe_allow_html=True)
    st.markdown("""
    - ✅ R-score calculator based on your Excel logic  
    - 📊 Biggest gains tool  
    - 🎯 Goals + semester countdown  
    - 💳 Stripe-ready premium upgrade  
    """)

        # ===== Free vs Premium =====
    st.markdown('<div class="section-title">Free vs. Premium</div>', unsafe_allow_html=True)
    st.markdown("""
        <style>
        /* Light & dark mode aware pricing cards */
        @media (prefers-color-scheme: light) {
            .pricing-wrapper { color: #0f172a; }
            .pricing-card {
                background: #ffffff;
                border: 1px solid #e2e8f0;
                border-radius: 1rem;
                box-shadow: 0 2px 6px rgba(0,0,0,0.05);
                transition: all 0.3s ease;
            }
            .pricing-header-free {
                background: #f8fafc;
                color: #0f172a;
                padding: 0.7rem 1rem;
                font-weight: 600;
                border-radius: 1rem 1rem 0 0;
            }
            .pricing-header-premium {
                background: #0f5fff;
                color: #ffffff;
                padding: 0.7rem 1rem;
                font-weight: 600;
                border-radius: 1rem 1rem 0 0;
            }
            .pricing-body { padding: 0.9rem 1.1rem; font-size: 0.95rem; }
        }

        @media (prefers-color-scheme: dark) {
            .pricing-wrapper { color: #e2e8f0; }
            .pricing-card {
                background: #1e293b;
                border: 1px solid #334155;
                border-radius: 1rem;
                box-shadow: 0 2px 8px rgba(0,0,0,0.6);
                transition: all 0.3s ease;
            }
            .pricing-header-free {
                background: #334155;
                color: #f1f5f9;
                padding: 0.7rem 1rem;
                font-weight: 600;
                border-radius: 1rem 1rem 0 0;
            }
            .pricing-header-premium {
                background: #0f5fff;
                color: #ffffff;
                padding: 0.7rem 1rem;
                font-weight: 600;
                border-radius: 1rem 1rem 0 0;
            }
            .pricing-body { padding: 0.9rem 1.1rem; font-size: 0.95rem; }
        }
        </style>

        <div class="pricing-wrapper">
            <div style="display:flex; gap:1rem; flex-wrap:wrap;">
                <div class="pricing-card" style="flex:1; min-width:250px;">
                    <div class="pricing-header-free">Free</div>
                    <div class="pricing-body">
                        <p>✔ Upload CSV manually</p>
                        <p>✔ One dashboard session</p>
                        <p>— OCR uploads</p>
                        <p>— Biggest gains ranking</p>
                        <p>— Goals + countdown</p>
                    </div>
                </div>
                <div class="pricing-card" style="flex:1; min-width:250px;">
                    <div class="pricing-header-premium">Premium</div>
                    <div class="pricing-body">
                        <p>✔ OCR + CSV + manual</p>
                        <p>✔ Unlimited sessions</p>
                        <p>✔ Biggest gains tab</p>
                        <p>✔ Goals + target R</p>
                        <p>✔ Stripe subscription</p>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


    # ===== About / How it works =====
    components.html(
        """
        <style>
        :root {
            --light-bg: #ffffff;
            --dark-bg: #1e293b;
            --light-text: #0f172a;
            --dark-text: #e2e8f0;
            --blue: #0f5fff;
            --gray-light: #475569;
        }

        @media (prefers-color-scheme: dark) {
            .rscore-box { background: var(--dark-bg); color: var(--dark-text); border: 1px solid #334155; }
        }
        @media (prefers-color-scheme: light) {
            .rscore-box { background: var(--light-bg); color: var(--light-text); border: 1px solid #e2e8f0; }
        }
        </style>

        <div style="font-family:'Inter',sans-serif;max-width:900px;margin:auto;">
            <h3 style="font-weight:600;color:var(--light-text);">How your R-score is calculated</h3>
            <div class="rscore-box" style="border-radius:1rem;padding:1.5rem 1.8rem;line-height:1.65;">
                <p><b>Your R-score reflects both your performance and the academic strength of your peers and school.</b></p>
                <p>Each of your courses has its own <i>individual R-score</i>, calculated using the official Québec CÉGEP formula:</p>
                <p style="font-size:1.1rem;color:var(--blue);"><b>R = ((Z × IDGZ) + ISGZ + C) × D</b></p>
                <ul style="margin-left:1rem;">
                    <li><b>Z</b> — How far your grade is from the class average, adjusted for spread (standard deviation).</li>
                    <li><b>IDGZ</b> — Measures the academic strength of your specific class group.</li>
                    <li><b>ISGZ</b> — Measures the overall strength of your high school or school board.</li>
                    <li><b>C</b> and <b>D</b> — Constants that keep scores within Québec’s official R-score range (C ≈ 35, D = 1).</li>
                </ul>
                <p>Once each course’s R-score is calculated, your <b>final or semester R-score</b> is weighted by course credits:</p>
                <p style="font-size:1.1rem;color:var(--blue);"><b>Final R = (Σ (R<sub>course</sub> × credits)) ÷ (Σ credits)</b></p>
                <p>That means higher-credit courses have a larger impact than smaller ones. RScoreCalc does this instantly when you upload your CSV — no setup required.</p>
                <p style="font-size:0.85rem;color:var(--gray-light);margin-top:1rem;">
                    <i>Based on official documentation from the Ministère de l’Enseignement supérieur and standard CÉGEP R-score methodology, adapted for transparency through RScoreCalc.</i>
                </p>
            </div>
        </div>

        <script>
        const resizeObserver = new ResizeObserver(entries => {
            for (let entry of entries) {
                window.parent.postMessage({
                    type: 'streamlit:setFrameHeight',
                    height: entry.contentRect.height + 20
                }, '*');
            }
        });
        resizeObserver.observe(document.body);
        </script>
        """,
        height=750,
        scrolling=False
    )

    # ===== Email signup =====
    st.markdown('<div class="section-title">Join the list</div>', unsafe_allow_html=True)
    st.markdown("Get notified when we add real college averages + mobile app.")
    with st.form("email_capture"):
        email = st.text_input("Email", placeholder="you@example.com")
        submitted = st.form_submit_button("Join the list")
        if submitted and email:
            st.success("You're on the list ✅")

    # ===== Footer =====
    st.markdown(
        """
        <div class="footer">
            <div>© rscorecalc.com</div>
            <div class="tos-link" onclick="window.parent.postMessage({ type: 'page', page: 'tos' }, '*')">Terms of Service</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


