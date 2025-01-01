import streamlit as st

# Profile Details
name = "John Doe"
title = "Software Engineer & Financial Enthusiast"
bio = (
    "Hello! I'm John Doe, a passionate developer with expertise in financial applications. "
    "I specialize in creating user-friendly tools to simplify complex calculations."
)
email = "johndoe@example.com"
github = "https://github.com/Vishwa0416/Mortgage-Payment-Application-"
linkedin = "https://www.linkedin.com/in/johndoe"
skills = ["Python", "Streamlit", "Matplotlib", "Pandas", "Machine Learning"]

# Streamlit Layout
st.title("👤 Profile")

# Profile Info
st.subheader(name)
st.text(title)
st.write(bio)

# Contact Info
st.write("📧", email)
st.write("🔗", f"[GitHub]({github})")
st.write("🔗", f"[LinkedIn]({linkedin})")

# Skills Section
st.write("### 🛠️ Skills")
for skill in skills:
    st.write("- ", skill)

# Footer
st.write("---")
st.write("Powered by Streamlit | [Mortgage Payment Application](https://github.com/Vishwa0416/Mortgage-Payment-Application-)")
