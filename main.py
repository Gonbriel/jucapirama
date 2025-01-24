from llama_index.llms.openai import OpenAI
from llama_index.core.agent.workflow import AgentWorkflow
import os
import asyncio
from dotenv import load_dotenv
from services import search_web

load_dotenv()

llm = OpenAI(model='gpt-4o-mini', api_key=str(os.getenv('OPENAI_KEY')))

async def main():
    while True:
        input_user = str(input('Input here: '))

        if input_user.lower() == 'exit':
            print('System out...')
            return

        workflow = AgentWorkflow.from_tools_or_functions(
            [search_web],
            llm=llm,
            system_prompt="You are a helpful assistant that can search the web for information.",
        )

        response = await workflow.run(user_msg=input_user)
        print(str(response))

if __name__ == '__main__':
    asyncio.run(main())