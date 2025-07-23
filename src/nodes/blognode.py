from src.states.blogState import BlogState
from langchain_core.messages import SystemMessage, HumanMessage
from src.states.blogState import Blog
from src.prompts.blogprompt import get_blog_prompt
from src.llms.OpenAIllm import Openllm

class BlogNode:
    """A class to represent the blog node"""

    def __init__(self, llm):
        self.llm = Openllm().get_llm("gpt-4o-mini")

    def blog_creation(self, state:BlogState) -> BlogState:
        topic = state['topic']
        
        prompt = get_blog_prompt()
        structuredmodel = self.llm.with_structured_output(Blog)

        chain = prompt | structuredmodel 
        response = chain.invoke({"topic":topic})
        state["blog"] = response
        return state


        


