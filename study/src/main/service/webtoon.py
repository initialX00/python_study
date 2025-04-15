from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#네이버 웹툰 크롤링하기 (정보 끌어모으기)

def run(): #파이썬은 생성자에 new를 쓰지 않는다
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #크롤링 세팅
    driver.get("https://comic.naver.com/webtoon?tab=mon") #사이트 정보 입력
    sleep(1) #바로 종료되기에 슬립으로 연장한다

    # wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li:nth-child(2) > a
    days = driver.find_elements(by=By.CSS_SELECTOR, value="#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul > li")
    for day in days[1:8]:
        print(day.text) #요일전체 월 화 수 목 금 토 일 매일+ 신작 완결 장르&
        link = day.find_element(by=By.CSS_SELECTOR, value="a")
        # selenium은 화면에 보이는 부분만 정보를 받아오기에 스크롤을 써야한다, 2번째 속성은 선택할 값을 의미한다
        driver.execute_script("arguments[0].scrollIntoView(true);", link)
        driver.execute_script("arguments[0].click()", link)
        sleep(2)