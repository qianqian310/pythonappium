"""L1雪球app实战演练"""
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestSearch:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.MainNestingActivity"
        caps["deviceName"] = "emulator-5554"
        caps["noReset"] = "true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    def test_search(self):
        """
        打开【雪球】应用首页
        点击搜索框（点击之前，判断搜索框的是否可用,并查看搜索框 name 属性值，并获取搜索框坐标，以及它的宽高）
        向搜索框输入:alibaba
        判断【阿里巴巴】是否可见
        如果可见，打印“搜索成功”
        如果不可见，打印“搜索失败
        """
        # 点击搜索框（点击之前，判断搜索框的是否可用,并查看搜索框 name 属性值，并获取搜索框坐标，以及它的宽高）
        select_box = self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/home_search")
        select_box_enable = select_box.is_enabled()
        select_box_att = select_box.get_attribute("name")
        select_box_loct = select_box.location
        size = select_box.size
        width = size.get("width")
        height = size.get("height")
        print(f"【搜索框】是否可用：{select_box_enable}，"
              f"它的 name属性值是：{select_box_att}，"
              f"它的坐标是：{select_box_loct},"
              f"它的宽是：{width}，它的高是：{height}")
        select_box.click()

        # 向搜索框输入:alibaba
        self.driver.find_element(AppiumBy.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        element_ali = self.driver.find_element(AppiumBy.XPATH, "//*[@text='阿里巴巴']")
        result = element_ali.is_displayed()
        if result == True:
            print("搜索成功 ")
            assert result == True
        else:
            print("搜索失败")
            assert result == False
