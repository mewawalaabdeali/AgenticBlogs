from typing import TypedDict, Optional, List
from pydantic import BaseModel, Field


class Blog(BaseModel):
    title:str=Field(description="the  tile of the blog post")
    content:str=Field(description="the main content of the blog post")

class BlogState(TypedDict, total=False):
    topic:str
    blog:Blog
    youtube_link:Optional[str]
    transcript: Optional[str]
    retriever_context: Optional[List[str]]
    web_results:Optional[str]
    draft: Optional[str]
    revised:Optional[str]
    approved:Optional[bool]
    published_url:Optional[str]
    user_feedback: Optional[List[str]]
    status: Optional[str]