from appium.webdriver.common.appiumby import AppiumBy

from assignment.wework_po.base.wework_page import WeworkPage


class HomePage(WeworkPage):
    _ADDRESS_BUT = (AppiumBy.XPATH, "//*[@text='通讯录']")

    def goto_address_page(self):
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        self.find_click(*self._ADDRESS_BUT)
        from assignment.wework_po.page.address_page import AddressPage
        return AddressPage(self.driver)
