# landing.py
import streamlit as st

def show_landing():
    st.set_page_config(page_title="RScoreCalc – Remove the mystery", layout="wide")

    st.markdown("### Built for Québec / CÉGEP students")
    st.markdown("## Remove the mystery around your R-score.")
    st.write(
        "RScoreCalc gives you instant R-score updates, shows you the biggest grade gains, "
        "and maps you to your target university program."
    )

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🧪 Try free calculator"):
            st.session_state["page"] = "free"
            st.rerun()
    with c2:
        if st.button("🔐 Go premium"):
            st.session_state["page"] = "auth"
            st.rerun()

    st.markdown("---")

    # free vs premium (you liked this)
    st.markdown("### Free vs. Premium")
    col_free, col_prem = st.columns(2)
    with col_free:
        st.markdown("#### Free")
        st.markdown("- Upload CSV manually")
        st.markdown("- 1 dashboard session")
        st.markdown("- Basic R-score view")
    with col_prem:
        st.markdown("#### Premium")
        st.markdown("- OCR + CSV + manual")
        st.markdown("- Unlimited sessions")
        st.markdown("- Biggest gains tab")
        st.markdown("- Goals + target R")
        st.markdown("- Stripe subscription")

    st.markdown("---")

    # ABOUT SECTION YOU ASKED FOR
    st.markdown("### How we estimate your R-score")
    st.markdown(
        """
We follow the public R-score structure used in Québec:

1. We extract **your mark**, **your group average**, and **your group standard deviation**.
2. We compute a standardized value: **Z = (your mark − group average) ÷ group SD**.
3. We adjust Z with your school’s **IDGZ** (indicator of group strength) and **ISGZ** (indicator of school strength) from our uploaded table.
4. We apply the working formula you chose:  
   **R = ((Z × IDGZ) + ISGZ + C) × D**, with C ≈ 35 and D = 1 to keep results in the CÉGEP R-score range.
5. When we don’t have an exact ISGZ/IDGZ for a school, we fall back to neutral values (IDGZ=1, ISGZ=0) so you still get a result.

Sources / logic we base this on:
- Ministère de l’Enseignement supérieur – documentation on the cote R
- Typical CÉGEP R-score formula structure (Z-score + school strength + constant)
- Your own uploaded CSV of school boards to refine IDGZ / ISGZ
        """
    )

    st.markdown("---")

    # email capture
    st.markdown("### Join the list")
    st.write("Get notified when we add real college averages and the mobile app.")
    email = st.text_input("Email")
    if st.button("Join"):
        st.success("You're on the list. (Wire this to Supabase later.)")

    # footer with ToS link
    st.markdown(
        """
        <div style='margin-top:2rem; font-size:0.8rem; color:#6b7280;'>
        © rscorecalc.com • <a href="?page=tos">Terms of service</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
