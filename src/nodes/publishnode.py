from src.states.blogState import BlogState
from src.states.blogState import Blog
from typing import List
import os
import requests
from dotenv import load_dotenv


class PublishNode:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("DEVTO_API_KEY")

    def publish_blog(self, state:BlogState)-> BlogState:
        blog:Blog=state["blog"]
        tags: List[str] = ["ai", "agents", "automation", "bloggen"]

        headers = {
            "api_key":self.api_key,
            "Content-Type": "application/json"
        }

        payload = {
            "article":{
                "title":blog.title,
                "published":True,
                "body_markdown":blog.content,
                "tags":tags
            }
        }

        response = requests.post("https://dev.to/api/articles", json=payload, headers=headers)

        if response.status_code==201:
            url = response.json()["url"]
            state["published_url"] = url
            state["status"] = "published"
            return state
        else:
            raise Exception(f"DEV.to publish failed: {response.status_code}, {response.text}")