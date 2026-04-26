# AI Phishing Detector

## Overview
This project is an AI-powered phishing detection tool that analyzes email content and determines whether it is likely safe or malicious.

It is designed to simulate how a cybersecurity analyst might quickly triage suspicious emails using AI assistance.

---

## Features
- Classifies emails as **Phishing** or **Safe**
- Provides a **confidence level**
- Highlights **key red flags**
- Gives a clear **explanation**
- Recommends **next actions**

---

## Why This Matters
Phishing attacks are one of the most common cybersecurity threats and are frequently used to steal credentials, deliver malware, and compromise systems.

This project demonstrates how AI can assist in:
- Identifying social engineering tactics
- Speeding up threat analysis
- Supporting decision-making in a security context

---

## Cybersecurity Use Case
This tool simulates a lightweight **Security Operations Center (SOC)** workflow where analysts must quickly evaluate suspicious emails.

It helps:
- Identify urgency-based or fear-based language
- Detect suspicious links or requests
- Provide actionable recommendations

---

## How It Works
1. User pastes an email into the app
2. The application sends the content to an AI model
3. The AI analyzes the email for phishing indicators
4. A structured response is returned and displayed

---

## Tech Stack
- Python
- Streamlit
- OpenAI API
- python-dotenv

---

## How to Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py

## Demo

### App Overview
![Overview](assets/app-overview.png)

---

### Safe Email Example
**Input:**
![Safe Input](assets/input-safe.png)

**Output:**
![Safe Output](assets/output-safe.png)

---

### Phishing Email Example
**Input:**
![Phishing Input](assets/input-phishing.png)

**Output:**
![Phishing Output](assets/output-phishing.png)