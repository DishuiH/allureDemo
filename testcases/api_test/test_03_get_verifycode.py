"""
获取验证码接口
"""
import pytest
import allure
from api.user import user
from common.logger import logger
from testcases.conftest import api_data

@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户管理模块")
class TestGetVerifyAPI:
    @allure.story("获取验证码接口")
    @allure.title("{title}")
    @pytest.mark.parametrize("title,email,optType,success,code,desc,reasonCode,reason,data",api_data["test_get_verifycode"][1])
    @pytest.mark.users
    def test_get_verifycode_01(self,title,email,optType,success,desc,code,reasonCode,reason,data):
        logger.info("*************** 开始执行用例 ***************")
        logger.info("发送邮箱号：{}，optType:{},查看接口返回".format(email,optType))
        res = user.get_verify_code(email,optType)
        assert res['success'] == success
        assert res['desc'] == desc
        assert res['code'] == code
        assert res['reasonCode'] == reasonCode
        assert res['reason'] == reason
        assert res['data'] == data

        expec_note = "获取验证码成功" if code == 200 else "获取验证码失败"
        actul_note = "获取验证码成功" if res['code'] == 200 else "获取验证码失败"
        logger.info("期望结果：{}， 实际结果：【 {} 】".format(expec_note, actul_note))
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("获取验证码接口")
    @allure.title("{title}")
    @pytest.mark.parametrize("title,email,optType,success,code,desc,reasonCode,reason,data",api_data["test_get_verifycode"][2])
    @pytest.mark.users
    def test_get_verifycode_02(self,title,email,optType,success,desc,code,reasonCode,reason,data):
        logger.info("*************** 开始执行用例 ***************")
        # test_get_verifycode_01已经发了2次
        LIMIT = 3
        with allure.step("5min内获取5次验证码"):
            for i in range(2,LIMIT+1):
                logger.info("5min内获取第{}次验证码".format(i))
                res = user.get_verify_code(email, optType)
                assert res['success'] == success
                assert res['desc'] == desc
                assert res['code'] == code
                assert res['reasonCode'] == reasonCode
                assert res['reason'] == reason
                assert res['data'] == data

        expec_note = "获取验证码成功" if code == 200 else "获取验证码失败"
        actul_note = "获取验证码成功" if res['code'] == 200 else "获取验证码失败"
        logger.info("获取到的编码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(expec_note, actul_note))
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("获取验证码接口")
    @allure.title("{title}")
    @pytest.mark.parametrize("title,email,optType,success,code,desc,reasonCode,reason,data",api_data["test_get_verifycode"][3])
    @pytest.mark.users
    def test_get_verifycode_03(self, title, email, optType, success, desc, code, reasonCode, reason, data):
        logger.info("*************** 开始执行用例 ***************")
        with allure.step("5min内第4次获取验证码"):
            logger.info("5min内获取第4次获取验证码")
            res = user.get_verify_code(email, optType)
            assert res['success'] == success
            assert res['desc'] == desc
            assert res['code'] == code
            assert res['reasonCode'] == reasonCode
            assert res['reason'] == reason
            assert res['data'] == data
            expec_note = "获取验证码失败，已达到获取验证码次数限制" if reasonCode == 2015 else "接口返回异常"
            actul_note = "获取验证码失败，已达到获取验证码次数限制" if res['reasonCode'] == 2015 else "接口返回异常"
            logger.info("获取到的编码 ==>> 期望结果：{}， 实际结果：【 {} 】".format(expec_note, actul_note))
            logger.info("*************** 结束执行用例 ***************")

    # @allure.story("获取验证码接口")
    # @allure.title("{title}")
    # @pytest.mark.parametrize("title,email,email_change,optType,success,desc,code,reasonCode,reason,data",api_data["test_get_verifycode_04"])
    # @pytest.mark.users
    # def test_get_verifycode_04(self, title, email,email_change,optType, success, desc, code, reasonCode, reason, data):
    #     logger.info("*************** 开始执行用例 ***************")
    #     with allure.step("5min内发送50次请求"):
    #         logger.info("5min内发送50次请求")
    #         IP_LIMIT = 50-4
    #         for i in range(IP_LIMIT):
    #             res = user.get_verify_code(email, optType)
    #         res = user.get_verify_code(email_change, optType)
    #         assert res['success'] == success
    #         assert res['desc'] == desc
    #         assert res['code'] == code
    #         assert res['reasonCode'] == reasonCode
    #         assert res['reason'] == reason
    #         assert res['data'] == data
    #         expec_note = "获取验证码失败，IP已被锁定" if reasonCode == 2015 else "接口返回异常"
    #         actul_note = "获取验证码失败，IP已被锁定" if res['reasonCode'] == 2015 else "接口返回异常"
    #         logger.info("期望结果：{}， 实际结果：【 {} 】".format(expec_note, actul_note))
    #         logger.info("*************** 结束执行用例 ***************")
if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_get_verifycode.py"])