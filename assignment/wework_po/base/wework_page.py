from appium import webdriver

from assignment.wework_po.base.base_page import BasePage


class WeworkPage(BasePage):
    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = '6'
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "emulator-5554"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        return self

    def end(self):
        pass

    def goto_main(self):
        from assignment.wework_po.page.home_page import HomePage
        return HomePage(self.driver)