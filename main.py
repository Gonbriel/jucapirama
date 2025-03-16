from llama_index.llms.gemini import Gemini
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import os
import asyncio
from dotenv import load_dotenv
from services import *

load_dotenv()

llm = Gemini(api_key=os.getenv('GEMINI_KEY'), model='models/gemini-2.0-flash')
Settings.llm = llm

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

async def main():

    print("Welcome! Type your question or 'exit' for quit.")

    workflow = AgentWorkflow.from_tools_or_functions(
            [search_web,
             import_csv,
             import_xlsx,
             csv_to_xlsx,
             csv_to_csv,
             rag],
            llm=llm,
            system_prompt = """Your goal is to clean tables for statistical analysis.

                                .Import the table.
                                .Identify if there is metadata in the first few rows and remove it.
                                .Adjust the header appropriately.
                                .Convert numeric values ​​that are in text.
                                .Use examples of clean tables whenever possible.
                                .Prioritize using RAG before making manual decisions."""

        )
    
    while True:
        input_user = str(input('\nInput here: ')).strip()

        if input_user.lower() == 'exit':
            print('System out...')
            break

        try:
            response = await workflow.run(user_msg=input_user)
            print('\nResponse:', response)
        
        except Exception as e:
            print(f'Error: {str(e)}. Try again.')

if __name__ == '__main__':
    asyncio.run(main())