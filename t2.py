from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import json
from bs4 import BeautifulSoup as bs
import requests


with open('info.json') as info:
    data = json.load(info)

username = data[0]
password = data[1]
school = 562
elevid = 29205685830
DRIVER_PATH = "chromedriver.exe"


class Driver():

    def __init__(self, password, username, school, elevid, driver_path):
        self.password = password
        self.username = username
        self.school = school
        self.elevid = elevid
        self.driver_path = driver_path
    
    def getWeek(self):
        info = []

        options = Options()
        options.headless = False
        options.add_argument("--window-size=600,600")
        driver = webdriver.Chrome(options=options, executable_path=self.driver_path)
        driver.get(f"https://www.lectio.dk/lectio/{self.school}/login.aspx")
        usernameInput = driver.find_element_by_xpath('/html/body/div[1]/form[2]/section/div[3]/div/section/div[2]/table/tbody/tr[2]/td[2]/input')
        passwordInput = driver.find_element_by_xpath('/html/body/div[1]/form[2]/section/div[3]/div/section/div[2]/table/tbody/tr[3]/td[2]/input')
        loginBtn = driver.find_element_by_xpath('/html/body/div[1]/form[2]/section/div[3]/div/table/tbody/tr/td/div/a')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        loginBtn.click()
        
        driver.get(f"https://www.lectio.dk/lectio/{self.school}/SkemaNy.aspx?type=elev&elevid={self.elevid}")
        sleep(1)
        soup = bs(driver.page_source, 'html.parser')
        #test = soup.find('div', class_="s2skemabrikcontent")
        divs = soup.find_all('a', class_="s2skemabrik s2bgbox s2withlink lec-context-menu-instance", href=True) + soup.find_all('a', class_="s2skemabrik s2bgbox s2changed s2withlink lec-context-menu-instance", href=True)
        

        # flot vector med links til alle moduler
        for a in divs:
            info.append("https://lectio.dk"+ a['href'])

        #hent data fra alle moduler :D
        for a in info:
            driver.get(a)
            soup = bs(driver.page_source, 'html.parser')

            test = soup.find_all('div', class_="s2skemabrikcontent")

            #for i in test:
            print(test[0])


            




driver = Driver(password, username, school, elevid, DRIVER_PATH)

driver.getWeek()


