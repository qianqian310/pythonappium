from faker import Faker

from Learning.L1.wework_po.page.wework_page import WeworkPage


class TestAddMembers:
    def setup_class(self):
        self.app = WeworkPage()
        self.faker = Faker("zh_CN")

    def setup(self):
        self.main = self.app.start().go_to_main()

    def test_add_members(self):
        name = self.faker.name()
        phone = self.faker.phone_number()
        toasts = self.main.goto_add_member_list().click_add_member().click_add_member_by_mou().save_member(name,
                                                                                                           phone).get_result_tips()
        assert '添加成功' == toasts
