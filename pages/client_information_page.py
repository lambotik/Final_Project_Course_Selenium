from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Client_Information_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:

    first_name = '//input[@id="first-name"]'
    last_name = '//input[@id="last-name"]'
    postal_code = '//input[@id="postal-code"]'
    button_continue = '//input[@id="continue"]'

    # Getters:
    # #Получаем методы через которые можем в будущем к ним обращаться

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_button_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_continue)))

    # Actions:
    # Выполняем необходимые действия с полученными полями
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print('Input first name')

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print('Input last name')

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print('Input postal code')

    def click_button_continue(self):
        self.get_button_continue().click()
        print('Click button continue')

    # Methods

    def input_information(self):
        self.get_current_url()
        self.input_first_name('Dima')
        self.input_last_name('Chernukha')
        self.input_postal_code('220100')
        self.click_button_continue()
