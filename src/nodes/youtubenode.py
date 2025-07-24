import streamlit as st
from langchain.schema import HumanMessage, SystemMessage
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from youtube_transcript_api import YouTubeTranscriptApi
import re
import requests
from dotenv import load_dotenv
import os
from src.states.blogState import BlogState
from typing import Optional

ytt_api = YouTubeTranscriptApi()

class TranscriptNode:
    def __init__(self):
        load_dotenv()

    def extract_video_id(self, url:str)->str:
        """To extract the video id of the url"""
        print(f"My link: {url}")
        self.patterns = [
            r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
            r'(?:embed\/)([0-9A-Za-z_-]{11})',
            r'(?:watch\?v=)([0-9A-Za-z_-]{11})',
            r'youtu\.be\/([0-9A-Za-z_-]{11})'
        ]
        for pattern in self.patterns:
            match = re.search(pattern, url)
            print(f"yeh wala abhi ka hai ")
            if match: return match.group(1) 
            
        return None
    def fetch_transcript(self, video_id:str)->str:
        """Use Youtube transcript api to fetch transcript"""
        try:
            print(f"youou: {video_id}")
            transcript = ytt_api.fetch(video_id)
            return ' '.join([item.text for item in transcript])
        except Exception as e:
            raise ValueError(f"Error fetching transcript: {e}")
        
    def generate_transcript(self, state:BlogState)->BlogState:
        
        self.youtube_link = state.get("youtube_link", "")
        if not self.youtube_link:
            raise ValueError("Youtube link is missing")
        self.video_id = self.extract_video_id(self.youtube_link)
        print(f"Video ID : {self.video_id}")
        transcript = self.fetch_transcript(self.video_id)

        state["transcript"] = transcript
        return state



