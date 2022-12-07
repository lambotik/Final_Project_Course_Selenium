from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Main_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:

    add_product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    add_product_2 = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    add_product_3 = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart = '//div[@id="shopping_cart_container"]'
    burger_menu = '//button[@id="react-burger-menu-btn"]'
    about = '//a[@id="about_sidebar_link"]'

    # Getters:
    # #Получаем методы через которые можем в будущем к ним обращаться

    def get_add_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_1)))

    def get_add_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_2)))

    def get_add_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu)))

    def get_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about)))

    # Actions:
    # Выполняем необходимые действия с полученными полями
    def click_add_product_1(self):
        self.get_add_product_1().click()
        print('Input Add Product: 1')

    def click_add_product_2(self):
        self.get_add_product_2().click()
        print('Input Add Product: 2')

    def click_add_product_3(self):
        self.get_add_product_3().click()
        print('Input Add Product: 3')

    def click_to_cart(self):
        self.get_cart().click()
        print('Click Cart')

    def click_burger_menu(self):
        self.get_burger_menu().click()
        print('Click Burger Menu')

    def click_about(self):
        self.get_about().click()
        print('Click About')

    # Methods

    def select_product_1(self):
        Logger.add_start_step(method='select_product_1')
        self.get_current_url()
        self.click_add_product_1()
        self.click_to_cart()
        Logger.add_end_step(url=self.driver.current_url, method='select_product_1')

    def select_product_2(self):
        Logger.add_start_step(method='select_product_2')
        self.get_current_url()
        self.click_add_product_2()
        self.click_to_cart()
        Logger.add_end_step(url=self.driver.current_url, method='select_product_2')

    def select_product_3(self):
        Logger.add_start_step(method='select_product_3')
        self.get_current_url()
        self.click_add_product_3()
        self.click_to_cart()
        Logger.add_end_step(url=self.driver.current_url, method='select_product_3')

    def select_burger_menu_about(self):
        Logger.add_start_step(method='select_burger_menu_about')
        self.get_current_url()
        self.click_burger_menu()
        self.click_about()
        self.assert_url('https://saucelabs.com/')
        Logger.add_end_step(url=self.driver.current_url, method='select_burger_menu_about')
