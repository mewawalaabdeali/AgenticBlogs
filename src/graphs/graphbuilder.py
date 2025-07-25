from langgraph.graph import StateGraph, START, END
from src.llms.OpenAIllm import Openllm
from src.states.blogState import BlogState
from src.nodes.blognode import BlogNode
from src.nodes.publishnode import PublishNode
from src.nodes.youtubeblog import YtBlogNode
from src.nodes.youtubenode import TranscriptNode
from src.nodes.retriever_context import retrieve_context
from src.nodes.websearch_node import WebSearchNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)

    def contentGraph(self):
        """Build a graph to generate blogs based on topic"""

        self.blog_nodeobj = BlogNode(self.llm)
        self.publish_nodeobj = PublishNode()
        print(self.llm)

        #Nodes
        self.graph.add_node("blog_creation", self.blog_nodeobj.blog_creation)
        self.graph.add_node("publish", self.publish_nodeobj.publish_blog)

        #Edges
        self.graph.add_edge(START, "blog_creation")
        self.graph.add_edge("blog_creation", "publish")
        self.graph.add_edge("publish", END)

        return self.graph
    
    def youtubeGraph(self):
        self.transcript_node = TranscriptNode()
        self.yt_blognode = YtBlogNode(self.llm)
        self.publishNode = PublishNode()
        self.retriever_node = retrieve_context
        self.web_node = WebSearchNode(self.llm)

        self.graph.add_node("fetch_transcript", self.transcript_node.generate_transcript)
        self.graph.add_node("retrieve_context", retrieve_context)
        self.graph.add_node("web_search", self.web_node.retrieve_and_search)
        self.graph.add_node("generate_blog", self.yt_blognode.blog_creation)
        self.graph.add_node("publishBlog", self.publishNode.publish_blog)

        self.graph.add_edge(START, "fetch_transcript")
        self.graph.add_edge("fetch_transcript", "retrieve_context")
        self.graph.add_edge("retrieve_context", "web_search")
        self.graph.add_edge("web_search", "generate_blog")
        self.graph.add_edge("generate_blog", "publishBlog")
        self.graph.add_edge("publishBlog", END)

        self.workflow = self.graph.compile(interrupt_before=["publishBlog"])

        return self.workflow


    
    def articlegraph(self):
        pass

    def setup_graph(self, usecase):
        if usecase == "title_blogs":
            self.contentGraph()
        elif usecase == "Youtube_transcript":
            self.youtubeGraph()
        elif usecase == "article_link":
            self.articlegraph()
        else:
            raise ValueError(f"Unknown use case: {usecase}")

        return self.graph.compile()
