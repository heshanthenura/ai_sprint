from googlesearch import search
links = list(search("vaccume cleaner", num_results=100,lang="en",region="lk",advanced=False))

for link in links:
    print(link)