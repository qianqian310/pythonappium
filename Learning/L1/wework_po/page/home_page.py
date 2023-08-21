from appium.webdriver.common.appiumby import AppiumBy

from Learning.L1.wework_po.page.wework_page import WeworkPage


class HomePage(WeworkPage):
    _ADDRESS_BOOK = (AppiumBy.XPATH, "//*[@text='通讯录']")

    def goto_add_member_list(self):
        # 1. 进入通讯录页面
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        self.find_click(*self._ADDRESS_BOOK)
        from Learning.L1.wework_po.page.add_member_list import AddMemberList
        return AddMemberList(self.driver)
