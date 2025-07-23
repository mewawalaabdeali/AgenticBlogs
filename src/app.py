import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.ui.streamlit.loadui import LoadStreamlitUI

ui = LoadStreamlitUI()
user_controls = ui.load_streamlit_ui()

if user_controls.get("OPENAI_API_KEY"):
    st.success("API key loaded successfully")