import pytest
from hamcrest import assert_that, close_to

from study.study2.xueqiu_po.base.xueqiu_page import XueQiuApp
from study.study2.xueqiu_po.utils import operate_yaml


class TestXueQiu:
    search_data = operate_yaml.get_data("../datas/searchdata.yaml")

    def setup_class(self):
        # 实例化雪球app，进行调用
        self.xueqiu_app = XueQiuApp()

    def setup(self):
        self.main = self.xueqiu_app.start().go_to_main_page()

    def teardown(self):
        self.xueqiu_app.stop()

    @pytest.mark.parametrize('search_key, search_assokey, price', search_data)
    def test_search(self, search_key, search_assokey, price):
        """
        打开【雪球】应用首页
        点击搜索框，进入搜索页面
        向搜索输入框中输入【alibaba】
        点击搜索结果中的【阿里巴巴】
        切换到 tab 的【股票】
        找到 股票【阿里巴巴】的股票价格 price
        判断 price 在 110 上下 10%浮动
        """
        search_key = "alibaba"
        search_assokey = "BABA"
        stock_price = self.main.click_search(). \
            input_search_content(search_key). \
            click_assokeys(search_assokey). \
            goto_stock_tab().get_price(search_assokey)

        # hamcres接近某个值
        assert_that(stock_price, close_to(price, price * 0.15))
