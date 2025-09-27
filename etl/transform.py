"""
This module transforms raw metadata from the Hacker News API into a structured format.
"""

from datetime import datetime
import trafilatura


def fetch_article_content(url):
    downloaded = trafilatura.fetch_url(url)
    return trafilatura.extract(downloaded) if downloaded else None


def sanitize_content_for_db(content):
    if content:
        return content.replace("'", "''").replace("\n", " ").strip()
    return ""


def transform_hacker_news_metadata(stories):
    transformed = []
    for story in stories:
        content = fetch_article_content(story.get("url")) if story.get("url") else ""
        sanitized_content = sanitize_content_for_db(content)
        transformed.append(
            {
                "title": story.get("title") or "",
                "author": story.get("by") or "",
                "url": story.get("url") or "",
                "points": story.get("score") or 0,
                "comments": story.get("descendants") or 0,
                "content": sanitized_content,
                "timestamp": datetime.fromtimestamp(story.get("time")).isoformat(),
            }
        )

    print(f"[{datetime.now()}] Transformed {len(transformed)} records.")

    return transformed
