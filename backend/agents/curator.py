import os
from datetime import datetime
from langchain.adapters.openai import convert_openai_messages
from .utils.chatbot import get_chatbot
import json

urls_sample_json = """
{
    "urls": [
        "https://example.com/article1",
        "https://example.com/article2",
        "https://example.com/article3"
    ]
}
"""

# Validate OpenAI API key is available
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please check your .env file.")

class CuratorAgent:
    def __init__(self):
        pass

    def curate_sources(self, query: str, sources: list, max_sources: int = 5):
        """
        Curate relevant sources for a query
        :param input:
        :return:
        """
        prompt = [{
            "role": "system",
            "content": f"You are a personal newspaper editor. Your sole purpose is to choose most relevant articles"
                       "for me to read from a list of articles.\n "
        }, {
            "role": "user",
            "content": f"Today's date is {datetime.now().strftime('%d/%m/%Y')}\n."
                       f"Topic or Query: {query}\n"
                       f"Your task is to return the {str(max_sources)} most relevant articles for me to read for the provided topic or "
                       f"query\n "
                       f"Here is a list of articles:\n"
                       f"{sources}\n"
                       f"Please return nothing but a JSON in the following format: {urls_sample_json}\n"
        }]
        
        chatbot = get_chatbot(model='openai/gpt-4.1-mini')
        
        response = chatbot.invoke(prompt).content
        
        chosen_sources = json.loads(response)["urls"]

        #print("response:", response)
        
        #print("typed response:", type(response))

        #print("response:", response)

        for i in sources:
            if i["url"] not in chosen_sources:
                sources.remove(i)
        
        #print(f"Curated sources: {sources}")
        
        #print("length of sources:", len(sources))
        #print("length of chosen sources:", len(chosen_sources))
        
        return sources

    def run(self, article: dict):
        article["sources"] = self.curate_sources(article["query"], article["sources"])
        return article
