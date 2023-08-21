from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class TestDemo:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def teardown_class(self):
        self.driver.quit()

    def test_sendkeys(self):
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="OS")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Morse Code")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/text")
        el4.clear()
        el4.send_keys("www.baidu.com")
        self.driver.back()
        self.driver.back()







