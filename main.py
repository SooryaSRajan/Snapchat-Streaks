import os

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
import webdriver_manager.chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from selenium.webdriver.support.select import Select

load_dotenv()

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")
option.add_argument("--window-size=1920x1080")
option.add_argument("--verbose")
caps = DesiredCapabilities().CHROME

driver = webdriver.Chrome(service=Service(webdriver_manager.chrome.ChromeDriverManager().install()), options=option,
                          desired_capabilities=caps)

driver.get('https://help.snapchat.com/hc/en-us/requests/new?ticket_form_id=149423&selectedAnswers=5695496404336640,'
           '5731111685324800')

friend_username = input('Enter your friend\'s username: ')

driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[3]/input").send_keys(os.getenv('USERNAME'))
driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[4]/input").send_keys(os.getenv('EMAIL'))
driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[5]/input").send_keys(os.getenv('NUMBER'))
driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[6]/input").send_keys(os.getenv('DEVICE'))
driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[7]/input").send_keys(friend_username)
driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[8]/input").send_keys(os.getenv('DATE'))
driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[9]/input").send_keys(os.getenv('STREAK'))
driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[11]/textarea").send_keys(os.getenv('DESC'))

while True:
    pass
