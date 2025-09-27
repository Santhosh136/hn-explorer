from etl.extract import extract_hacker_news_metadata
from etl.transform import transform_hacker_news_metadata
from etl.load import load_hacker_news_metadata
from config.constants import STORY_TYPES


def etl_process(story_type):
    stories = extract_hacker_news_metadata(story_type)
    transformed_stories = transform_hacker_news_metadata(stories)
    load_hacker_news_metadata(transformed_stories, story_type)


if __name__ == "__main__":
    story_types = STORY_TYPES
    for story_type in story_types:
        etl_process(story_type)
