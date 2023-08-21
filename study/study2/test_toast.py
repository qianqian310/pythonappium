from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestToast:
    """toast的获取和验证"""

    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".view.PopupMenu1"
        caps["deviceName"] = "emulator-5554"
        caps["noReset"] = "true"
        # appium 用的是uiautomator底层来抓取toast，使用的是uiautomator2
        # 再把toast放到控件树内，但是它本身不属于空间
        caps["automationName"] = "uiautomator2"
        url = "http://localhost:4723/wd/hub"

        self.driver = webdriver.Remote(url, caps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Search']").click()
        # print(self.driver.page_source)
        # self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text
        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'Clicked popup')]").text
