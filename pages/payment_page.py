from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Payment_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:

    button_finish = '//button[@id="finish"]'

    # Getters:
    # #Получаем методы через которые можем в будущем к ним обращаться
    def get_button_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_finish)))


    # Actions:
    # Выполняем необходимые действия с полученными полями
    def click_button_finish(self):
        self.get_button_finish().click()
        print('Click button finish')

    # Methods

    def payment(self):
        self.get_current_url()
        self.click_button_finish()
