from bs4 import BeautifulSoup
import requests
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
URL = "https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/"
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")

# Outer Tag Object
title = soup.find("span", attrs={"id":'productTitle'})

# Inner NavigableString Object
#title_value = title.string
# Title as a string value
#title_string = title_value.strip()

print(title)