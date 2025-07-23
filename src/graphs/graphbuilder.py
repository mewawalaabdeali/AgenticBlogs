from langgraph.graph import StateGraph, START, END
from src.llms.OpenAIllm import Openllm
from src.states.blogState import BlogState
from src.nodes.blognode import BlogNode
from src.nodes.publishnode import PublishNode

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
    
    def youtubGraph(self):
        pass
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
