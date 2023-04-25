# -*- coding: utf-8 -*-
# @Time : 2022/11/17 13:24
# @Author : Shawn Xiao
# @FileName: test_08_admin_login.py
# @Software: PyCharm
import pytest
import allure
from api.user import user
from common.logger import logger
from testcases.conftest import api_data
from common.redisUtil import redis_util

res = user.admin_login("admin.ailsa", "123456!Aa")
print(res)
# res = user.get_admin_access_token("admin.ailsa", "123456!Aa")
# print(res)