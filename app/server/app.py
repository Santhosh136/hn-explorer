from fastapi import FastAPI, Response
from logging import getLogger
from repo import execute_query
import uvicorn


app = FastAPI()
logger = getLogger(__name__)


@app.get("/top-stories")
async def get_top_stories():
    try:
        logger.info("Fetching top stories")
        # fetch data from SQLite database and return
        top_stories = execute_query(
            "SELECT title, author, url, points, comments, timestamp FROM stories ORDER BY points DESC LIMIT 10"
        )
        # FastAPI automatically handles JSON serialization for dicts/lists
        return {"stories": top_stories}
    except Exception as e:
        logger.error(f"Error fetching top stories: {e}")

        return Response(
            {"error": "Error fetching top stories"},
            media_type="application/json",
            status_code=500,
        )


def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run()
