import requests

headers = {
    'Authorization': 'Bearer jina_ab9334b81b614bafad287c1ed6e3acc8VTHAYsmy2M4s3E7Uhc6uVPKJhkZ8',
    'X-Retain-Images': 'none'
}
url = "https://appleasia.lk/product/iphone-12-2/"
response = requests.get(f'https://r.jina.ai/{url}', headers=headers)


print(response.text)
