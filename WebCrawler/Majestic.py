import httplib2
from bs4 import BeautifulSoup


header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}


def urls_to_visit():
    all_items_page = httplib2.Http()
    status, all_items_page_response = all_items_page.request('http://research.lunenfeld.ca/rtc/?page=List%20of%20Investigators',  headers=header)
    list_of_urls = []
    page = BeautifulSoup(all_items_page_response, "lxml")
    links = page.find_all("a")
    for link in links:
        if link.get('href').startswith('http://www.lunenfeld.ca/researchers/'):
            list_of_urls.append(str(link['href']))
    return list_of_urls

print(urls_to_visit())
links = urls_to_visit()
for link in links:
    all_items_page = httplib2.Http()
    status, all_items_page_response = all_items_page.request(link, headers=header)
    page = BeautifulSoup(all_items_page_response, "lxml")
    words = page.find_all("p")
    print(words)