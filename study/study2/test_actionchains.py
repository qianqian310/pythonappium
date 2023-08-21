# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
"""实现手机屏幕上滑动解锁7的造型"""

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class TestActionChains:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appium:deviceName"] = "emulator-5554"
        caps["appium:appPackage"] = "cn.kmob.screenfingermovelock"
        caps["appium:appActivity"] = "com.samsung.ui.FlashActivity"
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    def test_action_chains(self):
        # 设置手势
        el7 = self.driver.find_element(by=AppiumBy.ID, value="cn.kmob.screenfingermovelock:id/setPatternLayout")
        el7.click()
        # 定义ActionChains实例
        actions = ActionChains(self.driver)
        # 定义动作：按下--》滑动--》抬起
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(158, 237)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(467, 235)
        actions.w3c_actions.pointer_action.move_to_location(780, 235)
        actions.w3c_actions.pointer_action.move_to_location(780, 550)
        # 最后一个点
        actions.w3c_actions.pointer_action.move_to_location(780, 860)
        # 释放，手部抬起
        actions.w3c_actions.pointer_action.release()
        # 执行动作
        actions.perform()
