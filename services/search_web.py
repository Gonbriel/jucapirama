from tavily import AsyncTavilyClient
import os

async def search_web(query: str) -> str:
    """ Useful for using the web to answer questions. """
    print('Searching web...\n')
    client = AsyncTavilyClient(api_key=str(os.getenv('TAVILY_KEY')))
    return str(await client.search(query))