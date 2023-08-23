from appium.webdriver.common.appiumby import AppiumBy

from assignment.wework_po.base.wework_page import WeworkPage


class AddressPage(WeworkPage):
    _ADD_MEMBERS = (AppiumBy.XPATH, "//*[@text='添加成员']")

    def click_add_members(self):
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='添加成员']").click()
        self.find_click(*self._ADD_MEMBERS)
        from assignment.wework_po.page.add_members_page import AddMembersPage
        return AddMembersPage(self.driver)
