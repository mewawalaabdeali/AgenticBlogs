from RAG.ragPipe import BlogContextBuilder
from states.blogState import BlogState


sysprompt = """
            Retrieve from the store:
            - facts
            - summary
            - content to write a high quality blog"""

def retrieve_context(state:BlogState)->BlogState:
    transcript = state["transcript"]
    query = state.get("user_prompt", sysprompt)

    context_builder = BlogContextBuilder(transcript)
    context = context_builder.get_context(query)

    state["retriever_context"] = context
    return state