import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.llms.OpenAIllm import Openllm

import streamlit as st
from src.ui.streamlit.loadui import LoadStreamlitUI

ui = LoadStreamlitUI()
user_controls = ui.load_streamlit_ui()

#creating initial state
initial_state = {
    "topic": user_controls["topic"],
    "model_name":user_controls["selected_model"]

}

llm = Openllm().get_llm(initial_state["model_name"])
if user_controls.get("OPENAI_API_KEY"):
    st.success("API key loaded successfully")
if user_controls.get("topic") and user_controls.get("OPENAI_API_KEY"):
    if st.button("Generate Blog"):
        topic = initial_state["topic"]
        prompt = f"""Write a short blog on the topic: "{topic}".
        The blog should include:
        - A title
        - An engaging introduction
        - Two main points
        - A conclusion
        
        Write in a friendly, human language, professional tone."""

        response = llm.invoke(prompt)

        st.subheader("Generated Blog: ")
        st.markdown(response.content)