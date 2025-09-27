"""
This module loads transformed metadata into a relational database.
"""

from datetime import datetime
import sqlite3
import os


def load_hacker_news_metadata(transformed_stories):
    # Connect to SQLite database (or create it)
    # Get the directory of this script and construct absolute path to db
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "..", "db", "hacker_news.db")

    # Ensure the db directory exists
    db_dir = os.path.dirname(db_path)
    os.makedirs(db_dir, exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS stories (
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

    bulk_insert_query = """
        INSERT INTO stories (title, author, url, points, comments, content, timestamp) VALUES
    """

    for story in transformed_stories:
        bulk_insert_query += f"""(
            '{story.get("title")}',
            '{story.get("author")}',
            '{story.get("url")}',
            {story.get("points")},
            {story.get("comments")},
            '{story.get("content")}',
            '{story.get("timestamp")}'
        ),"""

    bulk_insert_query = bulk_insert_query.rstrip(",") + ";"

    cursor.execute(bulk_insert_query)

    conn.commit()
    conn.close()
