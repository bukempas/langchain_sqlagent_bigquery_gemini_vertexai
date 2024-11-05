#install packages
pip install -U langchain-google-genai

pip install langchain google-cloud-bigquery

pip install -U langchain-community

pip install sqlalchemy-bigquery

#get your Google AI API Key
import getpass
import os

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

#import libraries
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms import VertexAI
from langchain.schema import SystemMessage
import vertexai
import streamlit as st

#import generative ai for gemini pro from langchain google ai
from langchain_google_genai import GoogleGenerativeAI
llm = GoogleGenerativeAI(model="gemini-1.0-pro-001")

#langchain database tool and toolkits
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

# Replace with your BigQuery project ID and dataset
project_id = 'yourproject-id' #Google Cloud ProjectID
dataset_id = 'yourdataset-id' #Google Cloud Bigquery dataset-id

# Create a SQLDatabase instance
bigquery_db = SQLDatabase.from_uri(f"bigquery://{project_id}/{dataset_id}")
db=bigquery_db

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
toolkit.get_tools()
from langchain_community.tools.sql_database.tool import (
    InfoSQLDatabaseTool,
    ListSQLDatabaseTool,
    QuerySQLCheckerTool,
    QuerySQLDataBaseTool,
)

# Create the SQL agent
sql_agent = create_sql_agent(llm=llm, toolkit=toolkit, tools=toolkit.get_tools())

# Streamlit app
st.title("LangChain SQL Agent with BigQuery")

# User input for the query
user_query = st.text_input("Enter your query:")

# Run the agent and display the output
if st.button("Run Query"):
    if user_query:
        with st.spinner("Processing..."):
            try:
                response = agent.run(user_query)
                st.success(response)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a query.")

# Example usage with LangChain sql-agent without streamlit
user_question = "What is the average value of temperature reading from the sensor data of table?"
try:
    response = sql_agent.run(user_question)
    print(f"Agent's response:\n{response}")
except Exception as e:
    print(f"An error occurred: {e}")
