from langchain.prompts import PromptTemplate

def citation_prompt():
    prompt = PromptTemplate(
        template = 
        """You are an expert content researcher 20 years in the field.
        Use the following context to gather supporting facts from the internet using the tools available to you:
        - Wikipedia for encyclopedia-style summaries
        - Arxiv for academic research
        - Tavily for general web search

        Context: {retrieved_context}

        Return a concise, fact-rich set of citations that can support a high-quality blog post.""",
        input_variables=['retrieved_context'],
        validate_template=True
    )
    return prompt