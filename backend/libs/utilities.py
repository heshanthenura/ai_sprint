from googlesearch import search
import requests
import re
from bs4 import BeautifulSoup
from g4f.client import Client
import re
import json
import requests


def get_search_results(query, num_results = 100, lang="en", region="lk"):

    ecommerce_keywords = ["buy", "shop", "store", "product", "cart", "checkout", "sale", "offer"]

    links = list(search(query, num_results=num_results, lang=lang, region=region, advanced=False))

    ecommerce_urls = [
        url for url in links
        if any(keyword in url.lower() for keyword in ecommerce_keywords)
    ]

    return links



def fetch_url_content(url):
    # headers = {
    # 'Authorization': 'Bearer jina_ab9334b81b614bafad287c1ed6e3acc8VTHAYsmy2M4s3E7Uhc6uVPKJhkZ8',
    # 'X-Retain-Images': 'none'
    # }
    response = requests.get(f'https://r.jina.ai/{url}')
    return response.text

def scrape(url: str) ->str:
  response = requests.get(url)
  return response.text

def extract_price_blocks(text):

    keywords_pattern = r'\b(?:price|current price|USD|LKR|EUR|GBP|Rs.)\b|\bRs\s?\d+(?:\.d{1,2})?\b|\bRs.\s?\d+(?:\.d{1,2})?\b'
    
    blocks = text.split('\n')
    
    price_blocks = [block for block in blocks if re.search(keywords_pattern, block)]
    
    return price_blocks

def extract_text(response):
    soup = BeautifulSoup(response.text, 'html.parser')

    # # Remove all <img> tags from the HTML
    # for img_tag in soup.find_all('img'):
    #     img_tag.decompose()

    # # Extract the text from the remaining HTML
    # page_text = soup.get_text()
    return soup

def findloadableimage(img_url):
    try:
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            if img_url.endswith(".html"):
                return "https://www.svgrepo.com/show/325193/file-not-found.svg"
            else:
                return img_url

    except requests.exceptions.RequestException as e:
        print(f"Error loading image: {e}")
        return "https://www.svgrepo.com/show/325193/file-not-found.svg"

def extract_json(input_string):
    try:
        json_match = re.search(r'(\{.*\})', input_string, re.DOTALL)

        if json_match:
            json_string = json_match.group(1)
            parsed_json = json.loads(json_string)
            return parsed_json
        else:
            return {}
    except (json.JSONDecodeError, re.error) as e:
        # Return an empty dictionary if there's any error
        return {}