from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Cart_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:

    button_checkout = '//button[@id="checkout"]'

    # Getters:
    # #Получаем методы через которые можем в будущем к ним обращаться

    def get_button_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))

    # Actions:
    # Выполняем необходимые действия с полученными полями
    def click_button_checkout(self):
        self.get_button_checkout().click()
        print('Click Button Checkout')

    # Methods
    def product_confirmation(self):
        Logger.add_start_step(method='product_confirmation')
        self.get_current_url()
        self.click_button_checkout()
        Logger.add_end_step(url=self.driver.current_url, method='product_confirmation')
