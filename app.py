import streamlit as st
from password_checker import check_password_strength

st.set_page_config(page_title="ThreatGuardian AI", layout="centered")

st.title("🛡️ ThreatGuardian AI")
st.subheader("Your Free AI-Powered Cybersecurity Assistant")

selected = st.sidebar.radio("Select a feature", [
    "Home",
    "Password Strength Checker"
])

if selected == "Home":
    st.markdown("""
    Welcome to **ThreatGuardian AI** — a free cybersecurity toolset for students and professionals.

    🔐 Protect your passwords  
    💡 Learn about security strength  
    🧠 Use AI to make smarter security decisions
    """)

elif selected == "Password Strength Checker":
    st.subheader("🔐 Check Your Password Strength")

    password = st.text_input("Enter your password", type="password")

    if st.button("✅ Check Strength"):
        if password:
            strength, message = check_password_strength(password)
            st.info(f"**Strength:** {strength}")
            st.write(message)
        else:
            st.warning("Please enter a password to check.")
