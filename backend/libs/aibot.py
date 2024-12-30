from g4f.client import Client

def gpt(content,product):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": f"{content} from above,extract data about {product},and how prices and names,if discounts availabe show true. i only want csv with keys name,prince range,discount ,thats it"}],
    )
    return response.choices[0].message.content
