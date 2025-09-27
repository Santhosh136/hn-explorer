import streamlit as st
import requests

st.set_page_config(page_title="Hacker News Explorer", layout="wide")
st.title("📰 Hacker News Explorer")

# Tabs for different workflows
tab1, tab2, tab3 = st.tabs(["🔥 Best stories", "🆕 New Stories", "💼 Jobs"])

API_BASE = "http://localhost:8000"  # FastAPI base URL


def fetch_and_display_stories(story_type, title, error_msg):
    """
    Fetch stories from API and display them in Streamlit.

    Args:
        story_type (str): API endpoint suffix (e.g., 'beststories')
        title (str): Display title for the section
        error_msg (str): Error message if fetch fails
    """
    st.subheader(title)
    try:
        response = requests.get(f"{API_BASE}/stories/{story_type}")
        if not response.ok:
            st.error(error_msg)
            return

        stories = response.json().get("stories", [])

        if not stories:
            st.info("No stories available")
            return

        for story in stories:
            st.markdown(f"**[{story['title']}]({story['url']}) by {story['author']}**")

    except Exception as e:
        st.error(f"Error: {e}")


# Story configurations
story_configs = [
    ("beststories", "🚀 Best 10 Stories", "Failed to fetch Best stories"),
    ("newstories", "🆕 New 10 Stories", "Failed to fetch new stories"),
    ("jobstories", "💼 Job 10 Stories", "Failed to fetch job stories"),
]

# Display stories in tabs
tabs = [tab1, tab2, tab3]
for tab, (story_type, title, error_msg) in zip(tabs, story_configs):
    with tab:
        fetch_and_display_stories(story_type, title, error_msg)
