import logging

import yaml


def get_data(filename):
    logging.info("获取数据")
    with open(filename) as f:
        datas = yaml.safe_load(f)
        return datas
