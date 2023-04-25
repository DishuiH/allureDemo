"""
重置密码接口
"""

import pytest
import allure
from common.logger import logger
from api.user import user
from testcases.conftest import api_data,base_data
from common.redisUtil import redis_util
from common.mysql_operate import db


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户管理模块")
class TestResetPassAPI:

    @allure.story("重置密码接口")
    @allure.title("{title}")
    @pytest.mark.parametrize("title,email,password,success,code,desc,reasonCode,reason,data,expec_pass",api_data["test_reset_pass"])
    @pytest.mark.users
    @pytest.mark.usefixtures("insert_delete_user")
    def test_reset_pass(self,title,email,password,success,desc,code,reasonCode,reason,data,expec_pass):
        logger.info("*************** 开始执行用例 ***************")
        with allure.step("步骤1：获取邮箱验证码"):
            if reason == 'VerifyCode Empty.':
                verify_code = None
            elif reason in ['VerifyCode Error.','Email empty.','Pass empty.']:
                verify_code = 'hhhh'
            else:
                optType = "resetPass"
                name = "timekettle.markov.web.user.defence.code"
                key = ":resetPass"
                key = email + key
                user.get_verify_code(email=email, optType=optType)
                verify_code = redis_util.getHashData(name, key)
                if verify_code != 'null':
                    logger.info("邮箱{}获取得到验证码：{}".format(email,verify_code))
                else:
                    logger.info("邮箱{}获取不到验证码，请查找原因".format(email))
                if code == 200:
                    global USE_CODE
                    USE_CODE = verify_code
        with allure.step("步骤2：发送邮箱、密码、验证码，查看注册接口返回"):
            if title == "忘记密码_验证码已使用过":
                verify_code = USE_CODE
            if title == "忘记密码_使用验证码重置别人账号":
                email = "Timekettle@icloud.com"
            res = user.reset_pass(email,password,verify_code)
            assert res['success'] == success
            assert res['desc'] == desc
            assert res['code'] == code
            assert res['reasonCode'] == reasonCode
            assert res['reason'] == reason
            assert res['data'] == data
            logger.info("发送邮箱：{}，密码：{}，验证码：{}，接口返回{}".format(email, password,verify_code,res))


        with allure.step("步骤3：查看数据库中数据是否正确"):
            sql = base_data['register_sql']['select_register_user'][0]
            select_res = db.select_db(sql)
            try:
                new_pass = select_res[0]['password']
            except IndexError:
                new_pass = 'None'
            assert new_pass == expec_pass
        expec_note = "重置密码成功" if code == 200 else "重置密码失败"
        actul_note = "重置密码成功" if res['code'] == 200 else "重置密码失败"
        logger.info("接口测试结果 ==>> 期望结果：{}， 实际结果：【 {} 】".format(expec_note, actul_note))
        logger.info("*************** 结束执行用例 ***************")



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_06_reset_pass.py"])