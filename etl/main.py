from extract import extract_hacker_news_metadata
from transform import transform_hacker_news_metadata
from load import load_hacker_news_metadata

if __name__ == "__main__":
    stories = extract_hacker_news_metadata()
    transformed_stories = transform_hacker_news_metadata(stories)
    load_hacker_news_metadata(transformed_stories)
