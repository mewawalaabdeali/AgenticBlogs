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
for key in ["ready_to_publish", "publish_clicked", "published"]:
     if key not in st.session_state:
          st.session_state[key] = False

          
state:BlogState = {
            "topic":user_controls.get("topic", ""),
            "youtube_link":user_controls.get("youtube_link", "")
            }


#Tracking publish click in session
if "publish_clicked" not in st.session_state:
     st.session_state["publish_clicked"]=False

if user_controls.get("run_graph") and not st.session_state.get("ready_to_publish"):
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

            #Run initial graph(interrupted before publish)
            rstate = graph.invoke(state)

            if "next" in rstate and rstate["next"] == "publishBlog":
                 st.session_state["resume_state"] = rstate["messages"]
                 st.session_state["next_step"] = rstate["next"]
                 st.session_state["ready_to_publish"] = True


            #Display results:
            if "blog" in rstate:
                st.subheader(rstate["blog"].title)
                st.markdown(rstate["blog"].content)

#Show publish button only when ready
if st.session_state["ready_to_publish"] and not st.session_state["published"]:
     st.info("Blog Ready. Click below to Publish on to Dev.to")

     if st.button("Publish Blog"):
          st.session_state["publish_clicked"] = True

        
#Handle Publish floe
if st.session_state["publish_clicked"] and not st.session_state["published"]:

     #Resume graph
    llm = Openllm().get_llm(user_controls["selected_model"])
    graph = GraphBuilder(llm).setup_graph(user_controls["selected_usecase"])

    resume_state = st.session_state["resume_state"]
    next_step = st.session_state["next_step"]

    final_state = graph.invoke(resume_state, config={"next":next_step})

    st.success("Blog Published Successfully! 🚀")
    st.markdown(f"[Read your blog on DEV.to]({final_state['published_url']})")


    #Clean up session
    for key in ["resume_state", "next_step", "ready_to_publish", "publish_clicked"]:
        st.session_state.pop(key, None)
             







