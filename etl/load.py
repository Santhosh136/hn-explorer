"""
This module loads transformed metadata into a relational database.
"""

from datetime import datetime
import sqlite3
import os


def load_hacker_news_metadata(transformed_stories, story_type):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "..", "db", "hacker_news.db")

    db_dir = os.path.dirname(db_path)
    os.makedirs(db_dir, exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {story_type};")

    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {story_type} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            url TEXT,
            points INTEGER,
            comments INTEGER,
            content TEXT,
            timestamp DATETIME
        )
        """
    )

    for story in transformed_stories:
        cursor.execute(
            f"""
            INSERT INTO {story_type} (title, author, url, points, comments, content, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                story["title"],
                story["author"],
                story["url"],
                story["points"],
                story["comments"],
                story["content"],
                story["timestamp"],
            ),
        )

    conn.commit()
    conn.close()

    print(
        f"[{datetime.now()}] Loaded {len(transformed_stories)} records into {story_type} table."
    )
