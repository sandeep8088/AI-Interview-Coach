import streamlit as st
import openai

st.title("AI Interview Coach")

resume = st.text_area("Paste your Resume")
jd = st.text_area("Paste the Job Description")

if resume and jd:
    st.write("Generating interview questions...")
    st.success("Q1: Tell me about a project where you solved a technical challenge.\n\nTip: Align with the job's required skills.")