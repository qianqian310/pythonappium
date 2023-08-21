from appium.webdriver.common.appiumby import AppiumBy

from study.study2.xueqiu_po.base.xueqiu_page import XueQiuApp


class SearchPage(XueQiuApp):

    def input_search_content(self, search_key):
        # 输入搜索内容
        self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(search_key)
        return self

    def click_assokeys(self, text):
        self.driver.find_element(AppiumBy.XPATH, f"//*[@text='{text}']").click()
        from study.study2.xueqiu_po.page.search_result_page import SearchResultPage
        return SearchResultPage(self.driver)
