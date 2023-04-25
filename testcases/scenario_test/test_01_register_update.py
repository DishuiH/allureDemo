"""
新用户邮箱注册成功，修改昵称和查询用户信息
"""
import pytest
import allure
from common.logger import logger
from api.user import user

@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对业务场景测试")
@allure.feature("用户管理模块")
class TestRegister:
    @allure.story("邮箱注册接口-修改昵称接口-用户信息查询接口")
    @allure.title("新用户邮箱注册后修改昵称")
    @pytest.mark.users
    @pytest.mark.usefixtures("delete_register_user")
    def test_register_update(self,testcase_data):
        email = testcase_data['email']
        password = testcase_data['password']
        nickname = testcase_data['nickname']
        success = testcase_data['success']
        desc = testcase_data['desc']
        code = testcase_data['code']
        reason = testcase_data['reason']
        logger.info("*************** 开始执行用例 ***************")
        with allure.step("新用户邮箱注册成功"):
            res1 = user.email_register(email,password)
            id = res1['data']['id']
            token = res1['data']['authCode']
            assert res1['success'] == success
            assert res1['desc'] == desc
            assert res1['code'] == code
            assert res1['reason'] == reason
            assert res1['data']['email'] == email
            assert res1['data']['nickname'] == ""
        with allure.step("修改昵称为mm"):
            res2 = user.update_userinfo(token,id,nickname)
            assert res2['success'] == success
            assert res2['desc'] == desc
            assert res2['code'] == code
            assert res2['reason'] == reason
            assert res2['data']['id'] == id
            assert res2['data']['email'] == email
            assert res2['data']['nickname'] == nickname
        with allure.step("查询用户信息，昵称应为mm"):
            res3 = user.get_userinfo(token,id)
            assert res3['success'] == success
            assert res3['desc'] == desc
            assert res3['code'] == code
            assert res3['reason'] == reason
            assert res2['data']['id'] == id
            assert res2['data']['email'] == email
            assert res3['data']['nickname'] == nickname
            logger.info("获取到的昵称 ==>> 期望结果：{}， 实际结果：【 {} 】".format(nickname, res3['data']['nickname']))
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_register_update.py"])




