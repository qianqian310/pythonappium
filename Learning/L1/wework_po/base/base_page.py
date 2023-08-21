from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        """封装查找单个元素"""
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        """封装查找多个元素"""
        return self.driver.find_elements(by, locator)

    def find_click(self, by, locator):
        """封装查找并点击元素"""
        self.find(by, locator).click()

    def find_send_keys(self, text, by, locator):
        """封装查并给元素输入内容"""
        self.find(by, locator).send_keys(text)

    def set_implicitly_wait(self, time=1):
        """封装隐示等待时间"""
        self.driver.implicitly_wait(time)

    def get_tips(self):
        return self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text

