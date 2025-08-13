from langchain_tavily import TavilySearch
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_community.tools.arxiv.tool import ArxivQueryRun
from langchain.agents import Tool
from dotenv import load_dotenv

load_dotenv()


def get_webtools():
    """Returns a list of tools to be used in parallel during blog generation.
    These tools return relevant information based on the user query or context."""

    #Tavily tool(Google-like web search)
    tavily_tool = Tool(
        name = "Tavily Search",
        func=TavilySearch(max_result = 3),
        description="Use this tool to search the web for latest or supporting information"        
    )

    #Wikipedia Search tool
    wikipedia_tool = Tool(
        name="Wikipedia Search",
        func=WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper()),
        description="Use this tool to get encyclopedia-style summaries or historical facts"
    )

    #Arxiv search tool
    arxiv_tool = Tool(
        name="Arxiv Search",
        func=ArxivQueryRun(),
        description="Use this tool to fetch academic and technical research related to the topic"
    )

    tools = [tavily_tool, wikipedia_tool, arxiv_tool]

    return tools