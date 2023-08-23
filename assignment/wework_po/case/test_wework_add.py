from faker import Faker

from assignment.wework_po.base.wework_page import WeworkPage


class TestWeworkAdd:
    def setup_class(self):
        self.app = WeworkPage()
        self.main = self.app.start().goto_main()
        self.faker = Faker("zh_CN")

    def teardown_class(self):
        pass

    def test_add_member(self):
        name = self.faker.name()
        phone = self.faker.phone_number()
        tips = self.main.goto_address_page().\
            click_add_members().\
            add_members_by_hand().\
            save_members(name, phone).\
            get_res_tips()
        
        assert '添加成功' == tips
