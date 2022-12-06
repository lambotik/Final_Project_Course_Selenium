from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import Login_Page
from pages.main_page import Main_Page


def test_buy_product():
    s = Service('C:\\Users\\Дима\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    print('Start Test')

    login = Login_Page(driver)
    login.authorization()

    mp = Main_Page(driver)
    mp.select_burger_menu_about()

    print('Finish Test')
