from appium.webdriver.common.appiumby import AppiumBy

from Learning.L1.wework_po.page.wework_page import WeworkPage


class SaveMemberPage(WeworkPage):
    _ADD_NAME = (AppiumBy.XPATH, "//*[@text='姓名']/../*[@text='必填']")
    _ADD_PHONE = (AppiumBy.XPATH, "//*[@text='手机']/..//*[@text='必填']")
    _SAVE_BUTTON = (AppiumBy.XPATH, "//*[@text='保存']")

    def save_member(self, name, phone):
        # 4. 填写姓名
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='姓名']/../*[@text='必填']").send_keys(self.faker.name())
        self.find_send_keys(name, *self._ADD_NAME)
        # 5. 填写手机号
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='手机']/..//*[@text='必填']").send_keys(
        #     self.faker.phone_number())
        self.find_send_keys(phone, *self._ADD_PHONE)
        # 6. 点击保存按钮
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='保存']").click()
        self.find_click(*self._SAVE_BUTTON)

        from Learning.L1.wework_po.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
