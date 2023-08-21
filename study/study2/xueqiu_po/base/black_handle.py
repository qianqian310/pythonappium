import logging
import os
import traceback

import allure
from appium.webdriver.common.appiumby import AppiumBy

black_list = [(AppiumBy.ID, "com.xueqiu.android:id/ib_close")]


def black_wrapper(fun):
    def inner(*args, **kwargs):
        from study.study2.xueqiu_po.base.base_page import BasePage
        basepage: BasePage = args[0]
        try:
            logging.info(f"开始查找元素：{args[2]}")
            return fun(*args, **kwargs)
        except Exception as e:

            logging.info("未找到元素，异常正在处理中……")
            cur_time = basepage.get_time()
            time_name = cur_time + ".png"
            logging.info("当前保存图片的路径》》》" + os.path.dirname(__file__))
            # 拼接路径
            tmp_path = os.path.join(os.path.dirname(__file__), "..", "images", time_name)
            basepage.screenshot(tmp_path)

            allure.attach.file(tmp_path, "查找截图", attachment_type=allure.attachment_type.PNG)

            for e in basepage.black_list:
                logging.info(f"处理黑名单：{e}")
                # 查找黑名单里面的每一个元素
                ele = basepage.driver.find_elements(*e)
                if len(ele) > 0:
                    logging.info("点击黑名单弹框")
                    ele[0].click()
                    return fun(*args, **kwargs)

            logging.error(f"遍历黑名单，仍未找到元素，异常信息=====》{e}")
            logging.error(f"traceback.format_exc() =====》{traceback.format_exc()}")
            raise e

    return inner
