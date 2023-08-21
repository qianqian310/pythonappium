import time

from appium.webdriver.common.appiumby import AppiumBy

from study.study2.xueqiu_po.base.xueqiu_page import XueQiuApp


class MainPage(XueQiuApp):
    _SEARCH_BOX = (AppiumBy.ID, "com.xueqiu.android:id/title_height_view")

    def click_search(self):
        # 创建弹框，制造异常页面
        self.find_click(AppiumBy.XPATH,
                        "//*[@resource-id='com.xueqiu.android:id/action_message']/../../..//*[@resource-id='com.xueqiu.android:id/post_status']")

        time.sleep(5)
        # click search box 搜索框
        # self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/title_height_view").click()
        self.find_click(*self._SEARCH_BOX)
        from study.study2.xueqiu_po.page.search_page import SearchPage
        return SearchPage(self.driver)
