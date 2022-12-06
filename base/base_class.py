import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """"Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)

    """"Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f'Good value word = {value_word}')

    """"Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime(' %d.%m.%Y %H.%M.%S')
        """Создаем переменную screenshot к которой добавляем now_date(так мы получаем уникальное значение имени скриншота). Можно в название скриншота указывать имя конкретного теста к которому он относится"""
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(
            'C:\\Users\\Дима\\PycharmProjects\\Final Project Test Automation\\Final_Project_Course_Selenium\\screen\\' + name_screenshot)

    """"Method get current url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f'Good value url is: {result}')