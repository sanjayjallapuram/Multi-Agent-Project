from tools import web_search,scrape_url
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

#model setup
llm = ChatGroq(model="openai/gpt-oss-120b")

#1st agent
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
        system_prompt="""
            You are the Search Agent in a multi-agent research system.

            Your ONLY job is to search the web.

            You have exactly ONE available tool:
            - web_search

            IMPORTANT:
            - Always use web_search for web research.
            - NEVER call web_open.
            - NEVER call browser_search.
            - NEVER open URLs yourself.
            - NEVER scrape URLs yourself.
            - Do not invent or call any other tool.
            - After web_search returns results, return those search results.
            - The Reader Agent will handle URL scraping in the next step.

            Your task is complete after obtaining the search results.
            """
        )

#2nd agent
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url],
        system_prompt="""
            You are the Reader Agent in a multi-agent research system.

            Your job is to take the search results provided to you,
            identify the most relevant URL, and scrape that URL.

            You have exactly ONE available tool:
            - scrape_url

            IMPORTANT:
            - Use scrape_url to read the selected webpage.
            - NEVER call web_open.
            - NEVER call browser_search.
            - NEVER call web_search.
            - Do not invent or call any other tool.

            Return the useful content extracted from the webpage.
            """
    )
    

#writer chain
writer_prompt=ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

        Topic: {topic}

        Research Gathered:
        {research}

        Structure the report as:
        - Introduction
        - Key Findings (minimum 3 well-explained points)
        - Conclusion
        - Sources (list all URLs found in the research)

        Be detailed, factual and professional."""
    ),
])


writer_chain= writer_prompt | llm | StrOutputParser()


#critic chain
critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

        Report:
        {report}

        Respond in this exact format:

        Score: X/10

        Strengths:
        - ...
        - ...

        Areas to Improve:
        - ...
        - ...

        One line verdict:
        ..."""
    ),
])

critic_chain= critic_prompt | llm | StrOutputParser()
 