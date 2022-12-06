import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.cart_page import Cart_Page
from pages.login_page import Login_Page
from pages.main_page import Main_Page


@pytest.mark.run(order=2)
def test_buy_product_1():
    s = Service('C:\\Users\\Дима\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    print('Start Test 1')

    login = Login_Page(driver)
    login.authorization()

    mp = Main_Page(driver)
    mp.select_product_1()

    cp = Cart_Page(driver)
    cp.product_confirmation()

    # cip = Client_Information_Page(driver)
    # cip.input_information()
    #
    # p = Payment_Page(driver)
    # p.payment()
    #
    # f = Finish_Page(driver)
    # f.finish()
    print('Finish Test 1')


@pytest.mark.run(order=3)
def test_buy_product_2():
    #s = Service('C:\\Users\\Дима\\PycharmProjects\\resource\\chromedriver.exe')
    s = Service(r'C:\Users\Дима\PycharmProjects\resource\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    print('Start Test 2')

    login = Login_Page(driver)
    login.authorization()

    mp = Main_Page(driver)
    mp.select_product_2()

    cp = Cart_Page(driver)
    cp.product_confirmation()
    print('Finish Test 2')


@pytest.mark.run(order=1)
def test_buy_product_3():
    s = Service('C:\\Users\\Дима\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    print('Start Test 3')

    login = Login_Page(driver)
    login.authorization()

    mp = Main_Page(driver)
    mp.select_product_3()

    cp = Cart_Page(driver)
    cp.product_confirmation()
    print('Finish Test 3')
