from appium.webdriver.common.appiumby import AppiumBy

from assignment.wework_po.base.wework_page import WeworkPage


class SaveMembersPage(WeworkPage):
    _NAME = (AppiumBy.XPATH, "//*[@text='姓名']/../*[@text='必填']")
    _PHONE = (AppiumBy.XPATH, "//*[@text='手机']/..//*[@text='必填']")
    _SAVE_BUT = (AppiumBy.XPATH, "//*[@text='保存']")

    def save_members(self, name, phone):
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='姓名']/../*[@text='必填']").send_keys(name)
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='手机']/..//*[@text='必填']").send_keys(phone)
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='保存']").click()
        self.find_send_keys(name, *self._NAME)
        self.find_send_keys(phone, *self._PHONE)
        self.find_click(*self._SAVE_BUT)
        from assignment.wework_po.page.add_members_page import AddMembersPage
        return AddMembersPage(self.driver)
