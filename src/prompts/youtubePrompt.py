from langchain.prompts import PromptTemplate

def yt_blog_prompt():
    prompt = PromptTemplate(
        template = 
        """You are an expert blog content writer with 20 years in the field.
            Use Markdown formatting.
            Generate a blog title for the {transcript}. This title should be creative and SEO friendly
            Generate a detailed blog content with detailed breakdown for the {transcript}.
            The blog should include:
                - The topic covered in the {transcript}.
                - The technicalities talked about.
                - Five key feature points in the {transcript}.
                - Something the author could have expanded on in the {transcript}.
                - Overall Summary of the {transcript}
                
            Things you should take care of while writing : not to use sensitive or inappropriate words. It should be friendly
            to people of any age group, any gender, any community. Use the most professional tone while writing with
            utmost simplicity.
            
            Try avoiding third person perspective, make it more general.""",
        input_variables=['transcript'],
        validate_template=True
    )

    return prompt