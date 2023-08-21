"""app相关操作：start启动、restart重启、stop停止"""
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from study.study2.xueqiu_po.base.base_page import BasePage


class XueQiuApp(BasePage):
    def start(self):
        if self.driver ==  None:
            print("driver==None")
            caps = {}
            caps["platformName"] = "Android"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["deviceName"] = "emulator-5554"
            caps["noReset"] = "true"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            print("复用driver")
            self.driver.launch_app()
        return self

    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def go_to_main_page(self):
        from study.study2.xueqiu_po.page.main_page import MainPage
        return MainPage(self.driver)
