from asyncore import write
from calendar import c
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

data = []
list1 = []

driver = webdriver.Chrome()
wait = WebDriverWait(driver,36)
driver.maximize_window()
driver.get("https://www.teacheron.com/login.html")
time.sleep(3)
email = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[4]/div[3]/div/div[2]/div/div[1]/a[2]'))).click()
time.sleep(3)
E = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[4]/div[3]/div/div[2]/div/div[2]/div/div[1]/form/div[2]/div/input'))).send_keys("martimartial0@gmail.com")
P = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[4]/div[3]/div/div[2]/div/div[2]/div/div[1]/form/div[3]/div/input'))).send_keys("Add@1234")
time.sleep(2)
login = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[4]/div[3]/div/div[2]/div/div[2]/div/div[1]/form/div[4]/div[2]/div[2]/input'))).click()
time.sleep(5)
wait.until(EC.url_to_be("https://www.teacheron.com/myJobPosts"))

for page in range(1,2):
    driver.get("https://www.teacheron.com/tutors-in-nairobi?p="+ str(page))
    for i in range(1,21):
        URL = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[10]/div/div[3]/div/div[2]/div/div['+str(i)+']/div/div/ul/li/span/a'))).get_attribute('href')
        print(URL)
        data.append(URL)
        
    print(data)


for p in data:
    driver.get(p)
    time.sleep(2)
    name = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[5]/div[2]/div/h1/span[1]'))).text 
    print(name)
    list1.append(name)
    Url = driver.current_url
    print(Url)
    list1.append(Url)



rowHeader = ['TutorNames/URL']

df = pd.DataFrame(list1)
df.to_csv('Names.csv', index=False, header=rowHeader)