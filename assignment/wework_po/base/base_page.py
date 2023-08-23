from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_click(self, by, locator):
        self.find(by, locator).click()

    def find_send_keys(self, text, by, locator):
        self.find(by, locator).send_keys(text)

    def get_tips(self):
        # return self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text
        return self.find(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text
