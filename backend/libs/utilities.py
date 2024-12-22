from googlesearch import search
import requests


def get_search_results(query, num_results=100, lang="en", region="lk"):
    links = list(search(query, num_results=num_results, lang=lang, region=region, advanced=False))
    return links



def fetch_url_content(url):
    headers = {
    'Authorization': 'Bearer jina_ab9334b81b614bafad287c1ed6e3acc8VTHAYsmy2M4s3E7Uhc6uVPKJhkZ8',
    'X-Retain-Images': 'none'
    }
    response = requests.get(f'https://r.jina.ai/{url}', headers=headers)
    return response.text
