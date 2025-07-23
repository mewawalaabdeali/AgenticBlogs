from langchain.prompts import PromptTemplate

def get_blog_prompt():
    prompt = PromptTemplate(
        template = 
        """You are an expert blog content writer with 20 years in the field.
            Use Markdown formatting.
            Generate a blog title for the {topic}. This title should be creative and SEO friendly
            Generate a detailed blog content with detailed breakdown for the {topic}.
            The blog should include:
                - An engaging introduction paragraph with details
                - Two main points explaination as well
                - Positive aspects
                - Negative aspects
                - Work that can be done in the future
                - And conclusion""",
        input_variables=['topic'],
        validate_template=True
    )

    return prompt