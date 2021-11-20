"""
FILE: sample_semantic_search.py
DESCRIPTION:
    This sample demonstrates how to use semantic search.
USAGE:
    python sample_semantic_search.py
    Set the environment variables with your own values before running the sample:
    1) AZURE_SEARCH_SERVICE_ENDPOINT - the endpoint of your Azure Cognitive Search service
    2) AZURE_SEARCH_INDEX_NAME - the name of your search index (e.g. "hotels-sample-index")
    3) AZURE_SEARCH_API_KEY - your search API key
"""

import os

def speller():
    # [START speller]
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient
    endpoint="https://call-transcript-summarization-search.search.windows.net"

    # Getting the key:
    # az login
    # az search admin-key show --service-name call-transcript-summarization-search --resource-group przemek-cognitive-search

    key="6BC85FAECDA0320380FD338EC2E184C4"
    index_name = "hotels-sample-index"

    credential = AzureKeyCredential(key)
    client = SearchClient(endpoint=endpoint,
                          index_name=index_name,
                          credential=credential)
    results = list(client.search(search_text="luxucy", query_language="en-us", query_speller="lexicon"))

    for result in results:
        print("{}\n{}\n)".format(result["HotelId"], result["HotelName"]))
    # [END speller]

def semantic_ranking():
    # [START semantic_ranking]
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient

    endpoint="https://call-transcript-summarization-search.search.windows.net"
    key="6BC85FAECDA0320380FD338EC2E184C4"
    index_name = "hotels-sample-index"

    credential = AzureKeyCredential(key)
    client = SearchClient(endpoint=endpoint,
                          index_name=index_name,
                          credential=credential)
    results = list(client.search(search_text="luxury", query_type="semantic", query_language="en-us", semantic_fields="content"))

    for result in results:
        print("{}\n{}\n)".format(result["HotelId"], result["HotelName"]))
    # [END semantic_ranking]

if __name__ == '__main__':
    # speller()
    semantic_ranking()