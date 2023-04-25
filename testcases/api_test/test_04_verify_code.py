"""
验证验证码接口
"""

import pytest
import allure
from common.logger import logger
from api.user import user
from testcases.conftest import api_data,base_data
from common.redisUtil import redis_util


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户管理模块")
class TestVerifyCodeAPI:

    @allure.story("验证验证码接口")
    @allure.title("{title}")
    @pytest.mark.parametrize("title,email,password,optType,success,code,desc,reasonCode,reason,data",api_data["test_verify_code"])
    @pytest.mark.users
    @pytest.mark.usefixtures("delete_register_user")
    def test_verify_code(self,title,email,password,optType,success,code,desc,reasonCode,reason,data):
        logger.info("*************** 开始执行用例 ***************")
        with allure.step("步骤1：获取邮箱验证码"):
            if reason == 'VerifyCode Empty.':
                verifycode = None
            elif reason in ['VerifyCode Error.','Email empty.','OptType empty.']:
                verifycode = 'hhhh'
            else:
                name = "timekettle.markov.web.user.defence.code"
                if optType:
                    key = ":" + optType
                    key = email + key
                    user.get_verify_code(email=email, optType=optType)
                    verifycode = redis_util.getHashData(name, key)
                    if verifycode != 'null':
                        logger.info("邮箱{}获取得到验证码：{}".format(email,verifycode))
                    else:
                        logger.info("邮箱{}获取不到验证码，请查找原因".format(email))
                    if title == '验证码验证_验证码正确':
                        global USED_CODE
                        USED_CODE = verifycode
                    elif title == '验证码验证_重发验证码_输入新验证码':
                        global OLD_CODE
                        OLD_CODE = verifycode

        with allure.step("步骤2：发送邮箱、optType、验证码，查看验证接口返回"):
            if title == "验证码验证_重复使用验证码":
                verifycode = USED_CODE
            elif title in ['验证码验证_重发验证码_输入旧验证码','验证码验证_optType错误']:
                verifycode = OLD_CODE
            elif title == "验证码验证_输入别人收到的验证码":
                verifycode = OLD_CODE
                email = "Timekettle@icloud1.com"
            res = user.verify_code(email,verifycode,optType)
            assert res['success'] == success
            assert res['desc'] == desc
            assert res['code'] == code
            assert res['reasonCode'] == reasonCode
            assert res['reason'] == reason
            assert res['data'] == data
            logger.info("发送邮箱：{}，optType：{}，验证码：{}，接口返回{}".format(email, optType,verifycode,res))
            expec_note = "验证成功" if code == 200 else "验证失败"
            actul_note = "验证成功" if res['code'] == 200 else "验证失败"
            logger.info("验证验证码结果：{}， 实际结果：【 {} 】".format(expec_note, actul_note))

        if title == '验证码验证_验证码正确':
            with allure.step("步骤3：发送邮箱、optType、验证码，查看注册接口返回"):
                res = user.email_register(email,password,verifycode)
            expec_note = "注册成功" if code == 200 else "注册失败"
            actul_note = "注册成功" if res['code'] == 200 else "注册失败"
            logger.info("注册结果：{}， 实际结果：【 {} 】".format(expec_note, actul_note))
        logger.info("*************** 结束执行用例 ***************")



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_04_verify_code.py"])