import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.llms.OpenAIllm import Openllm
from src.nodes.blognode import BlogNode
from src.states.blogState import BlogState
import streamlit as st
from src.ui.streamlit.loadui import LoadStreamlitUI
from src.graphs.graphbuilder import GraphBuilder

ui = LoadStreamlitUI()
user_controls = ui.load_streamlit_ui()
state:BlogState = {
            "topic":user_controls.get("topic", ""),
            "youtube_link":user_controls.get("youtube_link", "")
            }

if user_controls.get("run_graph"):
        #CREATE INITIAL STATE:
        
        
        if not user_controls.get("OPENAI_API_KEY"):
             st.warning("Please enter your OPENAI API Key.")
        elif user_controls["selected_usecase"] == "title_blogs" and not state["topic"]:
             st.warning("Please enter a topic to generate blog")
        elif user_controls["selected_usecase"] == "Youtube_transcript" and not state["youtube_link"]:
             st.warning("Please enter a Youtube link")
        else:
             #Setup LLM, Graph, run
            llm = Openllm().get_llm(user_controls["selected_model"])
            graph_builder = GraphBuilder(llm)
            graph = graph_builder.setup_graph(user_controls["selected_usecase"])
            rstate = graph.invoke(state)
        


        

        #Display results:
        if "blog" in rstate:
            st.subheader(rstate["blog"].title)
            st.markdown(rstate["blog"].content)

        if "published_url" in rstate:
            st.success("Blog Published Successfully! 🚀")
            st.markdown(f"[Read your blog on DEV.to]({rstate['published_url']})")







