import os
from litellm import completion

# Validate OpenAI API key is available
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please check your .env file.")

# Get the model name from environment variables with a default fallback
DEFAULT_MODEL = "openai/gpt-4-mini"
MODEL_NAME = os.getenv("MODEL_NAME", DEFAULT_MODEL)

class Chatbot:
    def __init__(self, model=None, max_retries=1, **kwargs):
        """
        Initialize a chatbot instance.
        :param model: The model to use. If None, uses the MODEL_NAME from environment variable
        :param max_retries: Number of retries on failure. Defaults to 1
        :param kwargs: Additional arguments to pass to completion()
        """
        self.model = model if model is not None else MODEL_NAME
        self.max_retries = max_retries
        self.kwargs = kwargs

    def _convert_messages(self, messages):
        """
        Convert messages to the format expected by the LLM.
        :param messages: List of message objects or dicts
        :return: List of properly formatted message dicts
        """
        if not isinstance(messages, list):
            raise ValueError("Messages must be provided as a list")

        if all(isinstance(msg, dict) for msg in messages):
            return messages

        # Convert Langchain message objects to dicts
        converted_messages = []
        for msg in messages:
            if hasattr(msg, 'type') and hasattr(msg, 'content'):
                role = 'system' if msg.type == 'system' else 'user'
                converted_messages.append({"role": role, "content": msg.content})
            else:
                raise ValueError(f"Unsupported message type: {type(msg)}")
        return converted_messages

    def invoke(self, messages):
        """
        Make a completion API call with the given messages.
        :param messages: List of messages to send to the LLM
        :return: Response object with content attribute
        """
        converted_messages = self._convert_messages(messages)
        response = completion(
            model=self.model,
            messages=converted_messages,
            max_retries=self.max_retries,
            **self.kwargs
        )
        
        # Create a response object that mimics LangChain's ChatOpenAI response
        class Response:
            def __init__(self, content):
                self.content = content

        return Response(response.choices[0].message.content)

    def __call__(self, messages):
        """
        Make the class instance callable, maintaining backward compatibility.
        :param messages: List of messages to send to the LLM
        :return: Response from the revoke method
        """
        return self.revoke(messages)

def get_chatbot(model=None, max_retries=1, **kwargs):
    """
    Creates a Chatbot instance.
    :param model: The model to use. If None, uses the MODEL_NAME from environment variable
    :param max_retries: Number of retries on failure. Defaults to 1
    :param kwargs: Additional arguments to pass to completion()
    :return: A Chatbot instance
    """
    return Chatbot(model=model, max_retries=max_retries, **kwargs)
