from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

def rag(input: str):

    """
    Use this feature to try to answer any questions you don't know or don't have access to.
    
    Parameters:
    input (str): The user query.

    Returns:
    str: The response generated based on the available documents.
    """

    print('Searching for information...')
    
    documents = SimpleDirectoryReader('./data').load_data()
    index = VectorStoreIndex.from_documents(documents)

    query_engine = index.as_query_engine()
    response = query_engine.query(input)
    return response