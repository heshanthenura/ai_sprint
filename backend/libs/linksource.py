import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
driver_path = r"E:\Coding\Projects\ai_sprint\backend\libs\edgedriver_win64\msedgedriver.exe"
edge_service = Service(driver_path)


edge_options = Options()
edge_options.add_argument(f'user-agent={user_agent}')
edge_options.add_argument("--headless")  
edge_options.add_argument("disable-logging")

browser = webdriver.Edge(service=edge_service, options=edge_options)


browser.get('https://appleasia.lk/product/iphone-12-2/')
# Open the website
browser.get('https://python.org')




page_source = browser.page_source
print(page_source)

# Close the browser
browser.quit()