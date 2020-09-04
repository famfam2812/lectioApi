import re
import json
from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html

with open('info.json') as info:
    data = json.load(info)

class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17'


myopener = MyOpener()
#inffoooooo
school = 562
student = 29205685830
username = data[0]
password = data[1]

with Session() as s:
    site = s.get(f"https://www.lectio.dk/lectio/562/login.aspx")
    bs_content = bs(site.content, "html.parser")
    token = bs_content.find("input", {"name":"__EVENTVALIDATION"})["value"]
    login_data = {"m$Content$username": "chri93e6","m$Content$password": "bpn67zsg", "__EVENTVALIDATION":token}
    s.post("https://www.lectio.dk/lectio/562/login.aspx", login_data)

    home_page = s.get(f"https://www.lectio.dk/lectio/562/forside.aspx")
    print(home_page.content)
    print("\n" + token)


#m$Content$username
#m$Content$password


"""bs_content = bs(site.content, "html.parser")

#find token. Tokens bruges til at finde huske browsers og derefter give cookies så den kan se man faktisk er logget ind.
token = bs_content.find("input", {"id":"__EVENTVALIDATION"})["value"]
#print(token)

login_data = {"username": username, "password": password, "__EVENTVALIDATION":token}
requests.post(f"https://www.lectio.dk/lectio/{school}/login.aspx", login_data)

home_page = requests.get(f"https://www.lectio.dk/lectio/{school}/forside.aspx")

#print(home_page.content)
"""
"""
#def getter(school, student):
url = f"https://www.lectio.dk/lectio/{school}/SkemaNy.aspx?type=elev&elevid={student}"
PAGE = requests.get(url)

page = bs(PAGE.text, 'html.parser')

print(page.prettify())
for a in page.find_all('div', class_=' s2skemabrikcontainer lec-context-menu-instance'):
    print(a.prettify())

"""