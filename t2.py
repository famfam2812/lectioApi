from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import json

with open('info.json') as info:
    data = json.load(info)

username = data[0]
password = data[1]

school = 562
elevid = 29205685830

options = Options()
options.headless = False

options.add_argument("--window-size=600,600")


DRIVER_PATH = "chromedriver.exe"
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(f"https://www.lectio.dk/lectio/{school}/login.aspx")


usernameInput = driver.find_element_by_xpath('/html/body/div[1]/form[2]/section/div[3]/div/section/div[2]/table/tbody/tr[2]/td[2]/input')
passwordInput = driver.find_element_by_xpath('/html/body/div[1]/form[2]/section/div[3]/div/section/div[2]/table/tbody/tr[3]/td[2]/input')
loginBtn = driver.find_element_by_xpath('/html/body/div[1]/form[2]/section/div[3]/div/table/tbody/tr/td/div/a')


usernameInput.send_keys(username)
passwordInput.send_keys(password)
loginBtn.click()
driver.get(f"https://www.lectio.dk/lectio/{school}/SkemaNy.aspx?type=elev&elevid={elevid}")
skemaModuler = diver.find_element_by_xpath('/html/body/div[1]/form[2]/section/div[3]/div[2]/table/tbody/tr[4]/td[2]/div[1]/a[1]')
#print(usernamePath)
sleep(10)
driver.quit()