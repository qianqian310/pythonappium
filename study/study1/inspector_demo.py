import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXueQiu:
    def setup(self):
        desire_cap = {}
        # 平台
        desire_cap['platform'] = 'Android'
        # 设备名
        desire_cap['deviceName'] = 'emulator-5554'
        # app 包名
        desire_cap['appPackage'] = 'io.appium.android.apis'
        # app 页面名
        desire_cap['appActivity'] = '.ApiDemos'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        time.sleep(3)
        # 退出应用
        self.driver.quit()

    def test_api_demo(self):
        """
        1、打开 API demo apk
        2、点击 OS 控件
        3、点击 Morse Code 控件
        4、在搜索框中输入 ceshiren.com
        5、返回到第一页
        6、断言
        :return:
        """
        # 点击 OS 控件
        self.driver.find_element_by_accessibility_id("OS").click()
        # 点击 Morse Code 控件
        self.driver.find_element_by_accessibility_id("Morse Code").click()
        # 输入`ceshiren.com`
        self.driver.find_element_by_id("io.appium.android.apis:id/text").clear()
        self.driver.find_element_by_id("io.appium.android.apis:id/text").send_keys("ceshiren.com")
        # 返回第一页
        self.driver.back()
        self.driver.back()
        self.driver.back()
        # 选择元素进行断言
        result = self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='android:id/text1'][1]")
        print(result.text)
        # 断言
        assert result.text == "Access'ibility"