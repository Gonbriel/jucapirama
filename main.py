from llama_index.llms.openai import OpenAI
from llama_index.core.agent.workflow import AgentWorkflow
import os
import asyncio
from dotenv import load_dotenv
from services import search_web, import_csv, import_xlsx

load_dotenv()

llm = OpenAI(model='gpt-4o-mini', api_key=str(os.getenv('OPENAI_KEY')))

async def main():

    print("Welcome! Type your question or 'exit' for quit.")

    workflow = AgentWorkflow.from_tools_or_functions(
            [search_web],
            llm=llm,
            system_prompt=(
                "You are a helpful assistant. You can search the web if the user's question requires fresh information. "
                "Use your internal knowledge when possible, but if the question is about recent events, trends, or unknown topics, "
                "call the 'search_web' tool."
            ),
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