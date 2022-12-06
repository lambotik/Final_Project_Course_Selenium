from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import Login_Page
from pages.main_page import Main_Page
from pages.cart_page import Cart_Page
from pages.client_information_page import Client_Informayion_Page

def test_buy_product():
    s = Service('C:\\Users\\Дима\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    print('Start Test')

    login = Login_Page(driver)
    login.authorization()

    mp = Main_Page(driver)
    mp.select_product()

    cp = Cart_Page(driver)
    cp.product_confirmation()

    cip = Client_Informayion_Page(driver)
    cip.input_information()

    enter_shopping_cart = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
    enter_shopping_cart.click()
    print('Click Shopping Cart')
