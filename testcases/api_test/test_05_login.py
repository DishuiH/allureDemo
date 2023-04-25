"""
Login API
Editor: Shawn Xiao
"""
import pytest
import allure
from api.user import user
from common.logger import logger
from testcases.conftest import api_data
from common.redisUtil import redis_util

@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户管理模块")
class TestEmailLoginAPI:
    @allure.story("邮箱或ID登录接口")
    @allure.title("{title}")
    @pytest.mark.parametrize("title, username, Password, logintype, status_code, user_Id, errorId, message",
                             api_data["test_userIdOrEmail_login"])
    def test_email_login_01(self, title, username, Password, logintype, status_code, user_Id, errorId, message):
        logger.info("*************** 开始执行用例 ***************")
        logger.info("尝试登录邮箱：{}，密码：{}，查看接口返回".format(username, Password))
        res = user.email_login(username, Password, logintype)
        expec_note = "登录成功" if status_code == 200 else "登录失败"
        actul_note = "登录成功" if res.status_code == 200 else "登录失败"
        res_json = res.json()
        logger.info("期望结果：{}， 实际结果：【 {} 】".format(expec_note, actul_note))
        if res.status_code == 200:
            assert res_json['user'] == user_Id
            assert res_json['key']
            logger.info("*************** {} 断言成功  ***************" .format(title))

        else:
            assert res.status_code == status_code
            assert res_json['errorId'] == errorId
            assert res_json['message'] == message
            logger.info("*************** {} 断言成功  ***************" .format(title))

        logger.info("*************** 结束执行用例 ***************")

    @allure.story("SMS 登录接口")
    @allure.title("{title}")
    @pytest.mark.parametrize("title, phoneNumber, Password, logintype, status_code, user_Id, errorId, message",
                             api_data["test_phoneNumber_login"])

    def test_sms_login_02(self, title, phoneNumber, Password, logintype, status_code, user_Id, errorId, message):
        logger.info("*************** 开始执行用例 ***************")
        logger.info("尝试登录邮箱：{}，密码：{}，查看接口返回".format(phoneNumber, Password))
        res = user.sms_login(phoneNumber, Password, logintype)
        expec_note = "登录成功" if status_code == 200 else "登录失败"
        actul_note = "登录成功" if res.status_code == 200 else "登录失败"
        res_json = res.json()
        logger.info("期望结果：{}， 实际结果：【 {} 】".format(expec_note, actul_note))
        if res.status_code == 200:
            assert res_json['user'] == user_Id
            assert res_json['key']
            logger.info("*************** {} 断言成功  ***************".format(title))

        else:
            assert res.status_code == status_code
            assert res_json['errorId'] == errorId
            assert res_json['message'] == message
            logger.info("*************** {} 断言成功  ***************".format(title))

        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_05_login.py"])