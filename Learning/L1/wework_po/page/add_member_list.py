from appium.webdriver.common.appiumby import AppiumBy

from Learning.L1.wework_po.page.wework_page import WeworkPage


class AddMemberList(WeworkPage):
    _ADD_MEMBER_BUTTON = (AppiumBy.XPATH, "//*[@text='添加成员']")

    def click_add_member(self):
        # 2. 点击添加成员按钮
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='添加成员']").click()
        self.find_click(*self._ADD_MEMBER_BUTTON)
        from Learning.L1.wework_po.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
