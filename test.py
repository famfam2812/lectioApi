import re
import json
import requests
from bs4 import BeautifulSoup

school = 562
student = 29205685830

#def getter(school, student):
url = f"https://www.lectio.dk/lectio/{school}/SkemaNy.aspx?type=elev&elevid={student}"
PAGE = requests.get(url)

page = BeautifulSoup(PAGE.text, 'html.parser')

print(page.prettify())
for a in page.find_all('div', class_=' s2skemabrikcontainer lec-context-menu-instance'):
    print(a.prettify())



#getter(562, 29205685830)