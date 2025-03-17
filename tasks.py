from crewai import Task
from tools import web_tool
from agents import PostGenerationAgents
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Research Task
research_task = Task(
    description=(
        "Research the topic '{topic}' using available web sources."
        "Retrieve and analyze credible articles, reports, and insights to build a detailed understanding."
    ),
    expected_output="A well-structured, three-paragraph summary providing key insights, statistics, and references on '{topic}'.",
    tools=[web_tool],  
    agent=PostGenerationAgents().researcher_agent(),
)



writer_task = Task(
    description=(
        "Using the gathered information on '{topic}', craft a LinkedIn post"
        " in the user's preferred writing style: '{writing_style}'."
        " Ensure the post is engaging, informative, and includes relevant hashtags."
    ),
    expected_output="A well-structured, engaging LinkedIn post summarizing '{topic}' while maintaining the '{writing_style}' tone.",
    tools=[web_tool],  
    agent=PostGenerationAgents().writer_agent(),
    async_execution=False,
)
