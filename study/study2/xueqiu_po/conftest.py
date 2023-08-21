import os
import time

import pytest


# pytest可以直接获取rootdir的路径
def get_rootdir(request):
    # 根路径，默认认为有pytest.ini文件所在的路径为根路径
    rootdir = request.config.rootdir
    return rootdir


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = 'logs/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(os.path.join(get_rootdir(request), log_name))
