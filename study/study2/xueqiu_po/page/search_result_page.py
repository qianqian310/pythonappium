from appium.webdriver.common.appiumby import AppiumBy

from study.study2.xueqiu_po.base.xueqiu_page import XueQiuApp


class SearchResultPage(XueQiuApp):

    def goto_stock_tab(self):
        # 点击股票
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='股票']").click()
        return self

    def get_price(self, stock_num):
        # 找到对应的股票价格
        # 一般查找价格不一定能直接找到，需要通过xpath轴的方式去寻找
        current_price = self.driver.find_element(AppiumBy.XPATH,
                                                 f"//*[@text='{stock_num}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        return float(current_price)
