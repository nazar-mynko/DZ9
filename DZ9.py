import requests
from bs4 import BeautifulSoup


response = requests.get("https://ssu.gov.ua/")
if response.status_code == 200:
     soup = BeautifulSoup(response.text, features="html.parser")
     soup_list = soup.find_all("div", {"class" : "counter"})
for elem in soup_list:
    print(elem.text)
