# Extract metadata from Hacker News
"""
This module extracts metadata from the Hacker News API.
"""

from config.constants import HN_BASE_URL
from datetime import datetime
import requests

FETCH_STORIES_URL = HN_BASE_URL + "{}.json"
STORY_URL = HN_BASE_URL + "item/{}.json"


def extract_hacker_news_metadata(story_type):
    """
    Extracts metadata for top stories from Hacker News.
    Returns a list of dictionaries containing story metadata.
    """

    response = requests.get(FETCH_STORIES_URL.format(story_type))
    if response.status_code == 200:
        top_stories = response.json()
        # Fetch metadata for each top story
        metadata = []
        for story_id in top_stories[:10]:  # Limit to top 10 stories
            story_url = STORY_URL.format(story_id)
            story_response = requests.get(story_url)
            if story_response.status_code == 200:
                story_data = story_response.json()
                metadata.append(story_data)

        print(
            f"[{datetime.now()}] Extracted {len(metadata)} records from {story_type}."
        )

        return metadata
    else:
        print("Failed to retrieve top stories")
        return []
