"""
邮箱注册接口测试
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
class TestRegisterAPI:

    @allure.story("邮箱注册接口")
    @allure.title("{title}")
    @pytest.mark.parametrize("title,email,password,success,desc,code,reasonCode,reason,data,expec_register_type",api_data["test_email_register"])
    @pytest.mark.users
    @pytest.mark.usefixtures("delete_register_user")
    def test_email_register_01(self,title,email,password,success,desc,code,reasonCode,reason,data,expec_register_type):
        logger.info("*************** 开始执行用例 ***************")
        with allure.step("步骤1：获取邮箱验证码"):
            if reason == 'VerifyCode Empty.':
                verify_code = None
            elif reason in ['VerifyCode Error.','Email empty.','Pass empty.']:
                verify_code = 'hhhh'
            else:
                optType = "register"
                name = "timekettle.markov.web.user.defence.code"
                key = ":register"
                key = email + key
                user.get_verify_code(email=email, optType=optType)
                verify_code = redis_util.getHashData(name, key)
                if verify_code:
                    logger.info("邮箱{}获取得到验证码：{}".format(email,verify_code))
                else:
                    logger.info("邮箱{}获取不到验证码，请查找原因".format(email))
        with allure.step("步骤2：发送邮箱、密码、验证码，查看注册接口返回"):
            res = user.email_register(email,password,verify_code)
            assert res['success'] == success
            assert res['desc'] == desc
            assert res['code'] == code
            assert res['reasonCode'] == reasonCode
            assert res['reason'] == reason
            if res['data']:
                assert res['data']['email'] == data
            else:
                assert res['data'] == data
            logger.info("发送邮箱：{}，密码：{}，验证码：{}，接口返回{}".format(email, password,verify_code,res))

        with allure.step("步骤3：查看数据库中数据是否正确"):
            if email == "Timekettle@icloud.com":
                sql = base_data['register_sql']['select_register_user'][0]
            else:
                sql = base_data['register_sql']['select_register_user'][1]
            select_res = db.select_db(sql)
            try:
                register_type = select_res[0]['register_type']
            except IndexError:
                register_type = 'None'
            assert register_type == expec_register_type
        expec_note = "注册成功,数据库中新增用户" if code == 200 and register_type == 5 else "注册失败,数据库中没有新增用户"
        actul_note = "注册成功,数据库中新增用户" if res['code'] == 200 and register_type == 5 else "注册失败,数据库中没有新增用户"
        logger.info("接口测试结果 ==>> 期望结果：{}， 实际结果：【 {} 】".format(expec_note, actul_note))
        logger.info("*************** 结束执行用例 ***************")



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_register.py"])