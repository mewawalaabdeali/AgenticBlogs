from RAG.ragPipe import BlogContextBuilder
from states.blogState import BlogState

def retrieve_context(state:BlogState)->BlogState:
    transcript = state["transcript"]
    query = state.get("user_prompt", "Write a high-quality blog.")

    context_builder = BlogContextBuilder(transcript)
    context = context_builder.get_context(query)

    state["retriever_context"] = context
    return state