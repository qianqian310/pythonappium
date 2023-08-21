import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestContorlButton:

    def setup(self):
        # 创建一个字典，desirecapbility
        caps = {}
        caps["platformName"] = "Android"
        # Android 包名和页面名，获取命令：
        # mac/linux: adb logcat ActivityManager:I | grep "cmp"
        # windows: adb logcat ActivityManager:I | findstr "cmp"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["deviceName"] = "emulator-5554"
        caps["noReset"] = "true"

        # 创建driver ,与appium server建立连接，返回一个 session
        # driver 变成self.driver 由局部变量变成实例变量，就可以在其它的方法中引用这个实例变量了
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_id(self):
        """
        1、打开 demo.apk
        2、点击 Animation 进入下个页面
        3、点击 Seeking 进入下个页面
        4、查看【RUN】按钮是否显示/是否可点击
        5、查看【滑动条】是否显示/是否可用/是否可点击
        6、获取【滑动条】长度
        7、点击【滑动条】中心位置
        """
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Animation").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Seeking").click()

        # 4、查看【RUN】按钮是否显示 / 是否可点击
        ele_run = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Run")
        run_is_display = ele_run.is_displayed()
        run_is_clickable = ele_run.get_attribute("clickable")
        print(f"【run】按钮是否可显示：{run_is_display},是否可点击：{run_is_clickable}")

        # 5、查看【滑动条】是否显示 / 是否可用 / 是否可点击
        seek_bar = self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/seekBar")
        seek_bar_is_display = seek_bar.is_displayed()
        seek_bar_is_enabled = seek_bar.is_enabled()
        seek_bar_is_clickable = seek_bar.get_attribute("clickable")
        print(f"【滑动条】是否显示：{seek_bar_is_display}，"
              f"是否可用：{seek_bar_is_enabled}，"
              f"是否可点击：{seek_bar_is_clickable}")

        # 6、获取【滑动条】长度
        seekbar_size = seek_bar.size
        width = seekbar_size.get("width")
        print(f"【滑动条】的长度是：{width}")

        # 7、点击【滑动条】中心位置
        seekbar_location = seek_bar.location
        x = seekbar_location.get("x")
        y = seekbar_location.get("y")
        seekbar_centerx = x + width / 2
        seekbar_centery = y
        self.driver.tap([(seekbar_centerx, seekbar_centery)])
        time.sleep(5)
