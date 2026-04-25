import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Phishing Detector")

email_text = st.text_area("Paste suspicious email here:")

if st.button("Analyze"):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a cybersecurity analyst. Detect phishing emails and explain clearly."},
            {"role": "user", "content": f"""
Analyze this email and return:
1. Verdict (Phishing or Safe)
2. Confidence (Low/Medium/High)
3. Key red flags
4. Recommended action

Email:
{email_text}
"""}
        ]
    )

    st.write(response.choices[0].message.content)