from fastapi import FastAPI, Response
from logging import getLogger
from repo import execute_query
import uvicorn


app = FastAPI()
logger = getLogger(__name__)


@app.get("/stories/{story_type}")
async def get_stories(story_type: str):
    try:
        logger.info(f"Fetching {story_type} stories")
        # fetch data from SQLite database and return
        stories = execute_query(
            f"SELECT title, author, url, points, comments, timestamp FROM {story_type} ORDER BY points DESC LIMIT 10"
        )
        # FastAPI automatically handles JSON serialization for dicts/lists
        return {"stories": stories}
    except Exception as e:
        logger.error(f"Error fetching {story_type} stories: {e}")

        return Response(
            {"error": f"Error fetching {story_type} stories"},
            media_type="application/json",
            status_code=500,
        )


def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run()
