from tavily import TavilyClient
import os

# Get Tavily API key from environment variables
tavily_api_key = os.getenv("TAVILY_API_KEY")
if not tavily_api_key:
    raise ValueError("TAVILY_API_KEY environment variable is not set. Please check your .env file.")

tavily_client = TavilyClient(api_key=tavily_api_key)


def load_trusted_domains():
    """Load trusted AI news domains from configuration file."""
    domains = []
    domains_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "trusted_domains.conf")
    
    try:
        with open(domains_file, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines and comments
                if line and not line.startswith('#'):
                    domains.append(line)
    except FileNotFoundError:
        print(f"Warning: trusted_domains.conf file not found at {domains_file}")
        return []
    
    return domains


class SearchAgent:
    def __init__(self):
        self.trusted_domains = load_trusted_domains()

    def search_tavily(self, query: str):
        """
        Search for AI news using Tavily API with trusted domains filter.
        
        Args:
            query (str): The search query
            
        Returns:
            tuple: (list of search results, featured image URL)
        """
        results = tavily_client.search(
            include_images=True,
            query=query,
            topic="news",
            max_results=2,
           # include_domains=self.trusted_domains if self.trusted_domains else None
        )
                
        sources = results["results"]
        try:
            image = results["images"][0]
        except (KeyError, IndexError):
            image = "https://images.unsplash.com/photo-1542281286-9e0a16bb7366?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bmV3c3BhcGVyJTIwbmV3c3BhcGVyJTIwYXJ0aWNsZXxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&w=1000&q=80"
        
        return sources, image

    def run(self, article: dict):
        res = self.search_tavily(article["query"])        
        article["sources"] = res[0]
        article["image"] = res[1]

        return article
