import streamlit as st
import os

from src.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=" 🤖 " + self.config.get_pagetitle(), layout="wide")
        st.header(" 🤖 " + self.config.get_pagetitle())

        with st.sidebar:
            model_options = self.config.get_model_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls["selected_model"] = st.selectbox("SELECT MODEL", model_options)
            self.user_controls["selected_usecase"] = st.selectbox("SELECT USECASE", usecase_options)

            if self.user_controls["selected_usecase"] == "title_blogs":
                self.user_controls["topic"] = st.text_input("Enter the topic", "")
            elif self.user_controls["selected_usecase"] == "Youtube_transcript":
                self.user_controls["youtube_link"] = st.text_input("Please Enter the Youtube video link", "")
            else:
                self.user_controls["selected_usecase"] = st.text_input("Please enter the article link", "")


            self.user_controls["OPENAI_API_KEY"] = st.session_state["OPENAI_API_KEY"]=st.text_input("API KEY", type="password")
            self.user_controls["DEVTO_API_KEY"] = st.session_state["DEVTO_API_KEY"]=st.text_input("DEV.to API KEY", type="password")


            if not self.user_controls["OPENAI_API_KEY"] and not self.user_controls["DEVTO_API_KEY"]:
                st.warning("Please enter your API KEYs to proceed!")

            self.user_controls["run_graph"] = st.button("Generate Blog")

            

        return self.user_controls

            





