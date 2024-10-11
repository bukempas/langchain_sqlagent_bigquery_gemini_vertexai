# langchain_sqlagent_bigquery_gemini_vertexai
This repository demonstrates how to use a LangChain SQL agent to query Google Cloud BigQuery using the Gemini Generative AI through Vertex AI.   This allows you to interact with your BigQuery data using natural language, leveraging the power of Gemini's advanced language understanding capabilities.

## Setup

1. **Google Cloud Project:**
   - Create a Google Cloud project if you don't have one.
   - Enable the BigQuery and Vertex AI APIs.
   - Set up authentication (e.g., using a service account with appropriate permissions).

2. **Install Required Packages:**
   ```bash
   pip install langchain langchain-google-vertexai google-cloud-bigquery
3. Take attention to the costs of Google Cloud Bigquery and Vertex AI usages.


Key Components

LangChain: Provides the framework for building the SQL agent and interacting with the language model.

langchain-google-vertexai: Enables integration with Google's Vertex AI and Gemini API.

Google Cloud BigQuery: The data warehouse where your data is stored.

Gemini Pro API: A powerful large language model from Google that provides advanced natural language understanding.

Dataset used in Bigquery is obtained by Kaggle Datasets : https://www.kaggle.com/code/kerneler/starter-sensor-data-c5319b68-1
