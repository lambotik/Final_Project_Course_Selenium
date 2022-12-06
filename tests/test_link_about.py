from pages.cart_page import Cart_Page
from pages.client_information_page import Client_Informayion_Page
from pages.login_page import Login_Page
from pages.main_page import Main_Page
from pages.payment_page import Payment_Page
from pages.finish_page import Finish_Page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_buy_product():
    s = Service('C:\\Users\\Дима\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    print('Start Test')

    login = Login_Page(driver)
    login.authorization()

    mp = Main_Page(driver)
    mp.select_burger_menu_about()

    print('Finish Test')
