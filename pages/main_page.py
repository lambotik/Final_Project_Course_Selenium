from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Main_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:

    add_product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    cart = '//div[@id="shopping_cart_container"]'
    burger_menu = '//button[@id="react-burger-menu-btn"]'
    about = '//a[@id="about_sidebar_link"]'

    # Getters:
    # #Получаем методы через которые можем в будущем к ним обращаться

    def get_add_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_1)))

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
        print('Input add_product_1')

    def click_to_cart(self):
        self.get_cart().click()
        print('Click to cart')

    def click_burger_menu(self):
        self.get_burger_menu().click()
        print('Click burger menu')

    def click_about(self):
        self.get_about().click()
        print('Click About')

    # Methods

    def select_product(self):
        self.get_current_url()
        self.click_add_product_1()
        self.click_to_cart()

    def select_burger_menu_about(self):
        self.get_current_url()
        self.click_burger_menu()
        self.click_about()
        self.assert_url('https://saucelabs.com/')
