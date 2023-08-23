import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from faker import Faker
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class TestWework:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = '6'
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "emulator-5554"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        self.faker = Faker("zh_CN")

    def teardown_class(self):
        self.driver.quit()

    def test_add_members(self):
        """
        打开企业微信，不清空用户信息。
        进入到通讯录页面。
        点击添加按钮跳转到添加成员页面。
        点击手动输入添加，输入用户名、手机号，点击保存。
        保存跳转页面时，获取toast的文本信息。
        多断言：
            所有的成员姓名是否包含添加时输入的姓名；
            所有的成员手机号是否包含添加时输入的手机号；
            所有的成员邮箱是否包含添加时输入的邮箱。
            toast文本是否与预期结果一致。
        """
        name = self.faker.name()
        phone = self.faker.phone_number()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        time.sleep(5)

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(687, 1421)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(680, 992)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(10)

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='姓名']/../*[@text='必填']").send_keys(name)
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手机']/..//*[@text='必填']").send_keys(phone)
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='保存']").click()
        toast = self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text

        assert '添加成功' == toast