from g4f.client import Client


def get_gpt(text):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Extract the title, exact price or price range, and image url from the following webpage snippet into a JSON, which has elements such as title, price, and image_url. If you do not find relevant data for an element insert None to it.  I don't need extra text.\n {text}"}],
        # Add any other necessary parameters
    )
    return response.choices[0].message.content

# print(response.choices[0].message.content)