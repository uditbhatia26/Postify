from crewai import Agent
import os 
from dotenv import load_dotenv
from tools import web_tool
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

class PostGenerationAgents():
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o")


    # Creating a senior blog content Resarcher
    def researcher_agent(self):
        return Agent(
            role='Web Researcher & LinkedIn Post Generator',
            goal='Find relevant information from the web and craft an engaging LinkedIn post based on the user query: {query}',
            verbose=True,
            memory=True,
            backstory=(
                'An AI-driven researcher with expertise in sourcing relevant data from the web and '
                'structuring it into an engaging LinkedIn post that resonates with professionals.'
            ),
            llm=self.llm,
            tools=[web_tool],  
            max_iter=3,
            allow_delegation=True,
        )


    # Create a senior blog writer agent
    def writer_agent(self):
        return Agent(
            role='LinkedIn Post Writer',
            goal='Craft engaging and professional LinkedIn posts with relevant hashtags based on the insights gathered from {query}.',
            verbose=True,
            memory=True,
            backstory=(
                "A skilled LinkedIn content strategist who transforms research insights into compelling posts. "
                "With expertise in tech communication, you ensure every post is engaging, informative, and optimized with relevant hashtags."
            ),
            llm=self.llm,
            tools=[web_tool], 
            max_iter=3,
            allow_delegation=False,
        )


