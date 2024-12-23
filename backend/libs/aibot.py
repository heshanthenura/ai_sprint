from g4f.client import Client

with open('E:/Coding/Projects/ai_sprint/backend/libs/cleaned_text.txt', 'r', encoding='utf-8') as file: 
    content = file.read()

client = Client()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": f"{content} from above,extract data about iphones,and how prices and names,if discounts availabe show true. i only want json array with keys name,prince range,discount ,thats it"}],
)
print(response.choices[0].message.content) 