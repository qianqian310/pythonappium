from appium.webdriver.common.appiumby import AppiumBy

from assignment.wework_po.base.wework_page import WeworkPage


class AddMembersPage(WeworkPage):
    _ADD_BY_HAND = (AppiumBy.XPATH, "//*[@text='手动输入添加']")

    def add_members_by_hand(self):
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_click(*self._ADD_BY_HAND)
        from assignment.wework_po.page.save_members_page import SaveMembersPage
        return SaveMembersPage(self.driver)

    def get_res_tips(self):
        tips = self.get_tips()
        return tips
