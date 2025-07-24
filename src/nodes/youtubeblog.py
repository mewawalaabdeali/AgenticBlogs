from src.states.blogState import BlogState
from langchain_core.messages import SystemMessage, HumanMessage
from src.states.blogState import Blog
from src.prompts.youtubePrompt import yt_blog_prompt
from src.llms.OpenAIllm import Openllm
from src.nodes.retriever_context import retrieve_context
from src.tools.webTools import get_webtools
from src.prompts.webresultPrompt import citation_prompt
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

#contextobj = retrieve_context()
tools = get_webtools()

class YtBlogNode:
    """A class to represent the blog node"""

    def __init__(self, llm):
        self.llm = Openllm().get_llm("gpt-4o-mini")

    def retrieve_and_search(self,llm, state:BlogState)->BlogState:
        #Build context from transcript + query
        state = retrieve_context(state)
        context = state["retriever_context"]
        self.toolmodel = self.llm.bind_tools(tools)

        #get web results using tools
        parser = StrOutputParser()
        prompt = citation_prompt()

        chain = prompt | llm | parser
        response = chain.invoke({"retrieved_context":context})

        state["web_results"] = response

        
        return state
        



    def blog_creation(self, state:BlogState) -> BlogState:
        context = state["retriever_context"]
        web_result = state["web_results"]
        
        full_prompt_input = {
            "context":context,
            "web_results":web_result
        }

        prompt = yt_blog_prompt()
        structuredmodel = self.llm.with_structured_output(Blog)

        chain = prompt | structuredmodel 
        response = chain.invoke(full_prompt_input)
        state["blog"] = response
        return state