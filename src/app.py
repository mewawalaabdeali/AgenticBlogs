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

#creating initial state
state:BlogState = {
    "topic":user_controls["topic"],
}

llm = Openllm().get_llm(user_controls["selected_model"])
graph_builder = GraphBuilder(llm)
graph = graph_builder.setup_graph(user_controls["selected_usecase"])
rstate = graph.invoke(state)


#Display
st.subheader(rstate["blog"].title)
st.markdown(rstate["blog"].content)

st.success("Blog Published Successfully! 🚀")
st.markdown(f"[Read your blog on DEV.to]({rstate['published_url']})")