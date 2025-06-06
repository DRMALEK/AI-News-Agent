# GPT Newspaper (Forked Version - Bugs Fixed)

**Note**: This is a forked version of the original GPT Newspaper project with various bugs resolved and improvements made for better stability and functionality.

Welcome to the GPT Newspaper project, an innovative autonomous agent designed to create personalized newspapers tailored to user preferences. GPT Newspaper revolutionizes the way we consume news by leveraging the power of AI to curate, write, design, and edit content based on individual tastes and interests.

## 🔍 Overview

GPT Newspaper consists of six specialized sub-agents in LangChain's new [LangGraph Library](https://github.com/langchain-ai/langgraph):

1. **Search Agent**: Scours the web for the latest and most relevant news.
2. **Curator Agent**: Filters and selects news based on user-defined preferences and interests.
3. **Writer Agent**: Crafts engaging and reader-friendly articles.
4. **Critique Agent** Provide feedback to the writer until article is approved.
5. **Designer Agent**: Layouts and designs the articles for an aesthetically pleasing reading experience.
6. **Editor Agent**: Constructs the newspaper based on produced articles.
7. **Publisher Agent** Publishes the newspaper to the frontend or desired service

Each agent plays a critical role in delivering a unique and personalized newspaper experience.

<div align="center">
<img align="center" height="500" src="https://tavily-media.s3.amazonaws.com/gpt-newspaper-architecture.png">
</div>


## Demo
https://github.com/assafelovic/gpt-newspaper/assets/91344214/7f265369-1293-4d95-9be5-02070f12c67e


## 🌟 Features

- **Personalized Content**: Get news that aligns with your interests and preferences.
- **Diverse Sources**: Aggregates content from a wide range of reputable news sources.
- **Engaging Design**: Enjoy a visually appealing layout and design.
- **Quality Assurance**: Rigorous editing ensures reliable and accurate news reporting.
- **User-Friendly Interface**: Easy-to-use platform for setting preferences and receiving your newspaper.

## 🛠️ How It Works

1. **Setting Preferences**: Users input their interests, preferred topics, and news sources.
2. **Automated Curation**: The Search and Curator Agents find and select news stories.
3. **Content Creation**: The Writer Agent drafts articles, which are then designed by the Designer Agent.
4. **Newspaper Design**: The Editor Agent reviews and finalizes the content.
5. **Delivery**: Users receive their personalized newspaper to their mailbox.

## 🚀 Getting Started

### Prerequisites

- Tavily API Key - [Sign Up](https://tavily.com/)
- OpenAI API Key - [Sign Up](https://platform.openai.com/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your-username/gpt-newspaper.git
    ```
2. Set up your API Keys
   
   Copy the `.env.dist` file to `.env` and add your API keys:
   ```sh
   cp .env.dist .env
   ```
   
   Then edit the `.env` file and replace the placeholder values with your actual API keys:
   ```sh
   TAVILY_API_KEY=your_actual_tavily_api_key
   OPENAI_API_KEY=your_actual_openai_api_key
   MODEL_NAME=gpt-4-1106-preview  # Optional: Change the model to use
   ```
   
   Alternatively, you can export them as environment variables:
   ```sh
    export TAVILY_API_KEY=<YOUR_TAVILY_API_KEY>
    export OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
    ```
3. Install Requirements
   ```sh
   pip install -r requirements.txt
   ```
4. Validate your environment setup (optional but recommended)
   ```sh
   python validate_env.py
   ```
5. Run the app
   ```sh
    python app.py
    ```
6. Open the app in your browser
   ```sh
    http://localhost:5000/
    ```
6. Enjoy!

## 🤝 Contributing

Interested in contributing to GPT Newspaper? We welcome contributions of all kinds!


## 🛡️ Disclaimer

GPT Newspaper is an experimental project and provided "as-is" without any warranty. It's intended for personal use and not as a replacement for professional news outlets.
