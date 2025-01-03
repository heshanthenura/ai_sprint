from flask import Flask, render_template,request, Response
from libs.utilities import *
from libs.gpt4 import get_gpt
from bs4 import BeautifulSoup
import re



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form.get('search') 
    print(f"User Input: {user_input}")
    print(get_search_results(user_input))

    links = get_search_results(f'{user_input} price',10)

    parsed_objects = []
    # print(soup)
    # print(get_gpt(soup))
    print(len(links))

    for r in links:
        print("getting content ..")
        response = fetch_url_content(r)
        soup = BeautifulSoup(response, 'html.parser')
        print("gpt extracting ..")
        gpt_data = get_gpt(soup)
        print(gpt_data)
        # print(gpt_data)
        json_object = extract_json(gpt_data)
        print(f"imageURL before: {json_object}")
        
        if not json_object:
            continue

        keys = list(json_object.keys())

        price = str(json_object[keys[1]])

        if not (re.search(r'\d', price)):
            continue

        json_object[keys[2]] = findloadableimage(json_object[keys[2]])
        json_object['link'] = r
        print(json_object)
        parsed_objects.append(json_object)
        # parsed_objects = [json.loads(obj) for obj in json_objects]
    # parsed_objects = [{'title': 'iPhone 15 | Apple Asia', 'price': {'min': 219900, 'max': 449900}, 'imageURL': 'https://appleasia.lk/wp-content/uploads/2024/09/iPhone-15-All-Colours-%EF%A3%BF-110-300x300.jpg'}, {'title': 'Buy iPhone 15 and iPhone 15 Plus', 'price': 699, 'image_url': 'https://www.apple.com/shop/dc'}, {'title': 'iPhone 15', 'price': '', 'image_url': 'https://www.luxuryx.lk/_upload/17339447790.webp'}, {'title': 'Apple iPhone 15 Price in Sri Lanka | ikman', 'price': 'Rs 175,000', 'imageURL': 'https://i.ikman-st.com/u/apple-iphone-15-128gb-used-for-sale-colombo-724/8d817974-a20d-402f-9885-11a476766a92/160/120/cropped.webp'}, {'title': 'Apple iPhone 15 128GB', 'price': {'regular': 289900, 'sale': 224900}, 'imageUrl': 'https://celltronics.lk/wp-content/uploads/2023/09/Untitled-design-3-1-600x600.png'}, {'title': 'Apple iPhone 15 Pro Max | 512GB', 'price': '469,000.00~494,000.00~', 'image_url': 'https://geniusmobile.lk/wp-content/uploads/2023/09/iphone-15-pro-max-1-300x300.jpg'}, {'title': 'Apple iPhone 15 : Best price in Sri Lanka is Rs. 195,650', 'price': 195650, 'image_url': 'https://www.ideabeam.com/mobile/apple-iphone-15-price.html'}, {'title': 'Buy Apple iphone 15 for best price in Sri Lanka', 'price': 'Rs210,000.00', 'image_url': ''}, {'title': 'Best iPhone 15 Price in Sri Lanka | BuyAbans.com', 'price': {'from': 0, 'to': 999}, 'imageUrl': 'https://buyabans.com/storage/product/9698/new_pfgtghy_ect_2.png'}, {'title': 'Apple iPhone 15 128GB', 'price': 'Rs.206,500.00', 'image_url': 'https://lifemobile.lk/wp-content/uploads/2023/09/15-1.png'}]
    print(parsed_objects)
    return parsed_objects




@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

