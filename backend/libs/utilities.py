from googlesearch import search
import requests
from bs4 import BeautifulSoup
from g4f.client import Client



def get_search_results(query, num_results=10, lang="en", region="lk"):
    links = list(search(query, num_results=num_results, lang=lang, region=region, advanced=False))
    for l in links:
        print(l)
    return links

def get_webpage_source(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to fetch the webpage. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def remove_tags_preserve_text(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    return soup.get_text(separator='\n', strip=True)

def gpt(content, product, link):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": (
                    f"{content} from above, extract data about {product}, "
                    f"link is {link}, and return only a raw JSON array with no additional text or characters. "
                    f"Each item should have keys: name, price (numeric only), currency (e.g., 'LKR'), discount (boolean), and link."
                ),
            },
            {
                "role": "system",
                "content": "Do not use markdown or include any additional formatting.",
            }
        ],
    )
    
    raw_output = response.choices[0].message.content.strip()
    return(raw_output)



for l in get_search_results("iphone 12"):
    print(gpt(remove_tags_preserve_text(get_webpage_source(l)),"iphone 12",l))
    print()
    print()
    print()





