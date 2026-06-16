import streamlit as st
import google.generativeai as genai


genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🚀 AI Interview Question Generator")

role = st.text_input("Job Role")
skills = st.text_input("Skills")

difficulty = st.selectbox(
    "Difficulty",
    ["Beginner", "Intermediate", "Advanced"]
)

company = st.selectbox(
    "Target Company",
    ["Wipro", "TCS", "Infosys", "Accenture", "Google"]
)

if st.button("Generate Questions"):

    prompt = f"""
    Generate 5 {difficulty} interview questions
    for a {role} applying to {company}
    with skills {skills}.

    Give:
    1. Question
    2. Sample Answer
    3. Difficulty
    4. Interview Tips
    """

    response = model.generate_content(prompt)

    st.write(response.text)

    st.download_button(
        "Download Questions",
        response.text,
        file_name="interview_questions.txt"
    )
