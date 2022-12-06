from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Finish_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators:
    complete_order = '//h2[@class="complete-header"]'
    # Getters:
    def get_complete_order(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.complete_order)))
    # Actions:

    # Methods

    def finish(self):
        self.get_current_url()
        self.assert_word(self.get_complete_order(), 'THANK YOU FOR YOUR ORDER')
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')
        self.get_screenshot()
