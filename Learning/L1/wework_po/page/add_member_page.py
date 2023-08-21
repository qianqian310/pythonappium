from appium.webdriver.common.appiumby import AppiumBy

from Learning.L1.wework_po.page.wework_page import WeworkPage


class AddMemberPage(WeworkPage):
    _ADD_BY_HAND = (AppiumBy.XPATH, "//*[@text='手动输入添加']")
    _TIPS = (AppiumBy.XPATH, "//*[@class='android.widget.Toast']")

    def click_add_member_by_mou(self):
        # 3. 选择手工添加
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_click(*self._ADD_BY_HAND)
        from Learning.L1.wework_po.page.save_member_page import SaveMemberPage
        return SaveMemberPage(self.driver)

    def get_result_tips(self) -> str:
        # 7.等待弹窗获取弹窗信息
        # tips = self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']")
        tips = self.get_tips()
        return tips
