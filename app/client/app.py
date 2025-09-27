import streamlit as st
import requests

st.title("🔥 AI-Powered Hacker News Reader")

resp = requests.get("http://localhost:8000/top-stories")
stories = resp.json().get("stories", [])

for s in stories:
    st.subheader(s["title"])
    st.write(f"🔗 [Link]({s['url']}) | 👍 {s['points']} | 👤 {s['author']}")
