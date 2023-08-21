from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from faker import Faker


class TestWework:
    def setup(self):
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

    def teardown(self):
        self.driver.quit()

    def test_add_numbers(self):
        """
        实现在通讯录添加成员的功能
        """
        # 1. 进入通讯录页面
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()

        # 2. 点击添加成员按钮
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='添加成员']").click()
        # 3. 选择手工添加
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手动输入添加']").click()
        # 4. 填写姓名
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='姓名']/../*[@text='必填']").send_keys(self.faker.name())
        # 5. 填写手机号
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手机']/..//*[@text='必填']").send_keys(
            self.faker.phone_number())
        # 6. 点击保存按钮
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='保存']").click()
        # 7.等待弹窗获取弹窗信息
        toast = self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']")
        assert '添加成功' == toast
