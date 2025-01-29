from tavily import AsyncTavilyClient
import os

async def search_web(query: str) -> str:
    """ Useful for using the web to answer questions. """
    print('Searching web...\n')

    client = AsyncTavilyClient(api_key=str(os.getenv('TAVILY_KEY')))

    try:
        result = await client.search(query, search_depth='basic', max_results=3)

        structured_result = {
            "query": query,
            "top_results": [
                {"title": item['title'], "url": item['url'], "snippet": item['content']}
                for item in result['results']
            ]
        }
        return structured_result
    
    except Exception as e:
        return {'error': str(e)}