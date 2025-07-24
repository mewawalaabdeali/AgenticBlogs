from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.tools.arxiv.tool import ArxivQueryRun
from langchain.agents import Tool
def get_webtools():
    """Returns a list of tools to be used in parallel during blog generation.
    These tools return relevant information based on the user query or context."""

    #Tavily tool(Google-like web search)
    tavily_tool = Tool(
        name = "Tavily Search",
        func=TavilySearchResults(max_result = 3),
        description="Use this tool to search the web for latest or supporting information"        
    )

    #Wikipedia Search tool
    wikipedia_tool = Tool(
        name="Wikipedia Search",
        func=WikipediaQueryRun(),
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