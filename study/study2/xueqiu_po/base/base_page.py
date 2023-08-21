"""基本操作：例如初始化driver、click、find等"""
import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from study.study2.xueqiu_po.base.black_handle import black_wrapper


class BasePage:
    black_list = [(AppiumBy.ID, "com.xueqiu.android:id/ib_close")]

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

        # 异常处理放在每一个方法里，造成代码可维护性不高，需要抽离出来
        # try:
        #     return self.driver.find_element(by, locator)
        # except Exception as e:
        #     print("未找到元素，异常处理")
        #     for e in self.black_list:
        #         # 查找黑名单里面的每一个元素
        #         ele = self.driver.find_elements(*e)
        #         if len(ele) > 0:
        #             ele[0].click()
        #             return self.find(by, locator)
        #     raise e

    def find_click(self, by, locator):
        self.find(by, locator).click()

    def send_keys(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def find_get_text(self, by, locator):
        return self.find(by, locator).text

    def screenshot(self, name):
        # 添加截图
        self.driver.save_screenshot(name)

    def get_time(self):
        t = time.localtime(time.time())
        cur_time = time.strftime("%Y-%m-%d_%H_%M_%S", t)
        print(f"当前时间是：{cur_time}")
        return cur_time
