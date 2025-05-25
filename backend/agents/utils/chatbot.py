import os
from langchain_openai import ChatOpenAI

# Validate OpenAI API key is available
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please check your .env file.")

def get_chatbot(model='gpt-4.1-mini', max_retries=1, **kwargs):
    """
    Get a ChatOpenAI instance with the specified parameters.
    :param model: The model to use. Defaults to gpt-4-0125-preview
    :param max_retries: Number of retries on failure. Defaults to 1
    :param kwargs: Additional arguments to pass to ChatOpenAI
    :return: A ChatOpenAI instance
    """
    return ChatOpenAI(model=model, max_retries=max_retries, **kwargs)
