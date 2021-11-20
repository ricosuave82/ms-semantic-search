import json
import os
from typing import Mapping
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import requests

# index_name = "azureblob-index"
index_name = "hotels-sample-index"

# Get the service endpoint and API key from the environment
# endpoint = os.environ["SEARCH_ENDPOINT"]
# key = os.environ["SEARCH_API_KEY"]

endpoint="https://call-transcript-summarization-search.search.windows.net"

# Getting the key:
# az login
# az search admin-key show --service-name call-transcript-summarization-search --resource-group przemek-cognitive-search

key="6BC85FAECDA0320380FD338EC2E184C4"

# Create a client
credential = AzureKeyCredential(key)
client = SearchClient(endpoint=endpoint,
                      index_name=index_name,
                      credential=credential)


def add_document_to_index():
    doc_body = {
        'Category': 'Hotel',
        'hotelId': '1000',
        'rating': 4.0,
        'rooms': [],
        'hotelName': 'Azure Inn',
    }

    return client.upload_documents(documents=[doc_body])

def ms_search(search_text):

    results = client.search(search_text="hallo", query_type="semantic", query_language="en-us", search_fiels="content")
    return results

def ms_search_rest(search_text):

    endpoint = "https://call-transcript-summarization-search.search.windows.net/indexes/azureblob-index/docs?api-version=2020-06-30-Preview"
    body = { "search": "Where was Alan Turing born?",
        "queryType": "semantic",
        "searchFields": "title,url,body", 
        "queryLanguage": "en-us"
    }

    headers = { "api-key": key}

    response = requests.post(url=endpoint, data=body, headers=headers)
    print(response.status_code)
    print(response.content)
    print(response.reason)
    print(response.text)


if __name__ == "__main__":

    results = ms_search("hallo")
    # results = ms_search_rest("hallo")
    for result in results:
        print(json.dumps(result, indent=4))
