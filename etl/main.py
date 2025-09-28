from extract import extract_hacker_news_metadata
from transform import transform_hacker_news_metadata
from load import load_hacker_news_metadata


def etl_process(story_type):
    stories = extract_hacker_news_metadata(story_type)
    transformed_stories = transform_hacker_news_metadata(stories)
    load_hacker_news_metadata(transformed_stories, story_type)


if __name__ == "__main__":
    story_types = ["beststories", "newstories", "jobstories"]
    for story_type in story_types:
        etl_process(story_type)
