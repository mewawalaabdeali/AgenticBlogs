from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

class Openllm:
    def __init__(self):
        load_dotenv()
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

    def get_llm(self, model_name='gpt-4o'):
        try:
            print(os.getenv("OPENAI_API_KEY"))
            os.environ["OPENAI_API_KEY"] = self.openai_api_key = os.getenv("OPENAI_API_KEY")
            llm = ChatOpenAI(api_key=self.openai_api_key, model=model_name)
            return llm
        except Exception as e:
            raise ValueError("Error occured with exception: {e}")