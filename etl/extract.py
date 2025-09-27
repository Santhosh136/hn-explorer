# Extract metadata from Hacker News
"""
This module extracts metadata from the Hacker News API.
"""

import requests

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
STORY_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"


def extract_hacker_news_metadata():
    """
    Extracts metadata for top stories from Hacker News.
    Returns a list of dictionaries containing story metadata.
    """

    response = requests.get(TOP_STORIES_URL)
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
        return metadata
    else:
        print("Failed to retrieve top stories")
        return []
