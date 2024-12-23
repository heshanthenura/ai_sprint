from bs4 import BeautifulSoup
from linksource import getSource
def remove_tags_preserve_text(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    return soup.get_text(separator='\n', strip=True)

if __name__ == "__main__":
    # with open('E:/Coding/Projects/ai_sprint/backend/test/data.html', 'r', encoding='utf-8') as file:
    #     html_code = file.read()
    cleaned_text = remove_tags_preserve_text(getSource("https://appleasia.lk/product-category/iphone/"))
    with open('E:/Coding/Projects/ai_sprint/backend\libs/cleaned_text.txt', 'w', encoding='utf-8') as file:
        file.write(cleaned_text)
    print("Tags have been removed, and the text has been saved to 'cleaned_text.txt'")
