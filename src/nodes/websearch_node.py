from src.prompts.webresultPrompt import citation_prompt
from src.nodes.retriever_context import retrieve_context
from src.tools.webTools import get_webtools
from langchain_core.output_parsers import StrOutputParser
from src.states.blogState import BlogState
from src.llms.OpenAIllm import Openllm

class WebSearchNode:
    def __init__(self,llm):
        self.llm = llm
        self.tools = get_webtools()
        self.tool_model = self.llm.bind_tools(self.tools)
    
    def retrieve_and_search(self, state:BlogState)->BlogState:
        #Build context from transcript + query
        state = retrieve_context(state)
        context = state["retriever_context"]
        

        #get web results using tools
        parser = StrOutputParser()
        prompt = citation_prompt()

        chain = prompt | self.llm | parser
        response = chain.invoke({"retrieved_context":context})

        state["web_results"] = response

        
        return state
        