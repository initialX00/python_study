from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from dotenv import load_dotenv
import os

#로그인이 필요한곳에서의 크롤링

def run(): #파이썬은 생성자에 new를 쓰지 않는다
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #크롤링 세팅
    driver.get("https://koritbs.cafe24.com/student/index.php") #사이트 정보 입력
    driver.maximize_window() #전체화면
    sleep(1) #바로 종료되기에 슬립으로 연장한다

    usernameInput = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr:nth-child(3) > td > input")
    passwordInput = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-0.border-top-0.bg-brown > td > input")
    usernameInput.send_keys(os.getenv("TMS_USERNAME"))
    passwordInput.send_keys(os.getenv("TMS_PASSWORD"))

    loginButton = driver.find_element(by=By.CSS_SELECTOR, value="body > div > form > table > tbody > tr.border-left-danger.border-right-danger.border-bottom-danger.border-top-0.bg-brown > td > div > div:nth-child(2) > button")
    driver.execute_script("arguments[0].scrollIntoView(true)", loginButton)
    driver.execute_script("arguments[0].click()", loginButton)
    sleep(5)






