import re
import json
import requests
from bs4 import BeautifulSoup as bs

#inffoooooo
school = 562
student = 29205685830
username = "chri93e6"
password = "bpn67zsg"

site = requests.get(f"https://www.lectio.dk/lectio/{school}/login.aspx")
bs_content = bs(site.content, "html.parser")

#find token. Tokens bruges til at finde huske browsers og derefter give cookies så den kan se man faktisk er logget ind.
token = bs_content.find("input", {"id":"__EVENTVALIDATION"})["value"]
print(token)

login_data = {"username": username, "password": password, "__EVENTVALIDATION":token}
requests.post(f"https://www.lectio.dk/lectio/{school}/login.aspx", login_data)

home_page = requests.get(f"https://www.lectio.dk/lectio/{school}/forside.aspx")

print(home_page.content)

"""
#def getter(school, student):
url = f"https://www.lectio.dk/lectio/{school}/SkemaNy.aspx?type=elev&elevid={student}"
PAGE = requests.get(url)

page = bs(PAGE.text, 'html.parser')

print(page.prettify())
for a in page.find_all('div', class_=' s2skemabrikcontainer lec-context-menu-instance'):
    print(a.prettify())

"""