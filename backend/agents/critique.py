import os
from datetime import datetime
from langchain.adapters.openai import convert_openai_messages
from .utils.chatbot import get_chatbot

# Validate OpenAI API key is available
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please check your .env file.")

class CritiqueAgent:
    def __init__(self):
        pass

    def critique(self, article: dict):
        prompt = [{
            "role": "system",
            "content": "You are a newspaper writing critique. Your sole purpose is to provide short feedback on a written "
                       "article so the writer will know what to fix.\n "
        }, {
            "role": "user",
            "content": f"Today's date is {datetime.now().strftime('%d/%m/%Y')}\n."
                       f"{str(article)}\n"
                       f"Your task is to provide a really short feedback on the article only if necessary.\n"
                       f"if you think the article is good, please return None.\n"
                       f"if you noticed the field 'message' in the article, it means the writer has revised the article"
                        f"based on your previous critique. you can provide feedback on the revised article or just "
                       f"return None if you think the article is good.\n"
                        f"Please return a string of your critique or None.\n"
        }]

        lc_messages = convert_openai_messages(prompt)
        
        chatbot = get_chatbot(model='gpt-4.1-mini')
        response = chatbot.invoke(lc_messages).content
        
        if response == 'None':
            return {'critique': None}
        else:
            print(f"For article: {article['title']}")
            print(f"Feedback: {response}\n")
            return {'critique': response, 'message': None}

    def run(self, article: dict):
        article.update(self.critique(article))
        return article
