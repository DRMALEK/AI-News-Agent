import os
import time
from concurrent.futures import ThreadPoolExecutor
from langgraph.graph import Graph

# Import agent classes
from .agents import SearchAgent, CuratorAgent, WriterAgent, DesignerAgent, EditorAgent, PublisherAgent, CritiqueAgent


class MasterAgent:
    def __init__(self):
        self.output_dir = f"outputs/run_{int(time.time())}"
        os.makedirs(self.output_dir, exist_ok=True)

    def run(self, queries: list, layout: str):
        
        # Initialize agents
        search_agent = SearchAgent() # source counts, source filters
        
        curator_agent = CuratorAgent()
        
        # scraper agenet


        # Summariser agent (level 1, 2, 3, etc. - different levels of summarisation)
        
        # Writer agent (with different writing styles, e.g., news, blog, etc.)

        writer_agent = WriterAgent()
        #critique_agent = CritiqueAgent()
        designer_agent = DesignerAgent(self.output_dir)
        editor_agent = EditorAgent(layout)
        publisher_agent = PublisherAgent(self.output_dir)

        # Define a Langchain graph
        workflow = Graph()

        # Add nodes for each agent
        
        
        # Search agenet: This agent will search for articles based on the queries provided
        workflow.add_node("search", search_agent.run)
        
        # Curator agent: This agent will curate the articles found by the search agent, and return 5 most relevant articles depending on the query
        workflow.add_node("curate", curator_agent.run)
        
        # 
        workflow.add_node("write", writer_agent.run)
        #workflow.add_node("critique", critique_agent.run)
        workflow.add_node("design", designer_agent.run)

        # Set up edges
        workflow.add_edge('search', 'curate')
        workflow.add_edge('curate', 'write')
        workflow.add_edge('write', 'design')
        #workflow.add_edge('write', 'critique')
        # workflow.add_conditional_edges(source='critique',
        #                                path=lambda x: "accept" if x['critique'] is None else "revise",
        #                                path_map={"accept": "design", "revise": "write"})

        # set up start and end nodes
        workflow.set_entry_point("search")
        workflow.set_finish_point("design")

        # compile the graph
        chain = workflow.compile()

        # Execute the graph for each query in parallel
        with ThreadPoolExecutor() as executor:
            parallel_results = list(executor.map(lambda q: chain.invoke({"query": q}), queries))

        # Compile the final newspaper
        newspaper_html = editor_agent.run(parallel_results)
        newspaper_path = publisher_agent.run(newspaper_html)

        return newspaper_path
