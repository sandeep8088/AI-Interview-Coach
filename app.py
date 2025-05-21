import streamlit as st
import openai
import os

st.title("AI Interview Coach")

openai.api_key = os.getenv("OPENAI_API_KEY")

resume = st.text_area("Paste your Resume")
jd = st.text_area("Paste the Job Description")

if resume and jd:
    prompt = f"Given the following resume and job description, generate 3 mock interview questions with improvement suggestions:\n\nResume:\n{resume}\n\nJob Description:\n{jd}"
    with st.spinner("Generating interview questions..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.success(response.choices[0].message["content"])
