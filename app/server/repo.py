def get_db_connection():
    import os
    import sqlite3

    # Get the directory of this script and construct absolute path to db
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(script_dir, "../..", "db", "hacker_news.db")

    # Ensure the db directory exists
    db_dir = os.path.dirname(db_path)
    os.makedirs(db_dir, exist_ok=True)

    conn = sqlite3.connect(db_path)
    return conn


def close_db_connection(conn):
    conn.close()


def execute_query(query, params=()):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()

        # Get column names for better JSON formatting
        columns = [description[0] for description in cursor.description]

        # Convert to list of dictionaries
        formatted_results = []
        for row in results:
            formatted_results.append(dict(zip(columns, row)))

        conn.commit()
        close_db_connection(conn)
        return formatted_results
    except Exception as e:
        if conn:
            close_db_connection(conn)
        raise e
