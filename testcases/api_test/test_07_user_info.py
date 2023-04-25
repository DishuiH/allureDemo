"""
更新用户昵称接口,还没开始写
"""
import pytest
import allure
from api.user import user
from common.logger import logger
from testcases.conftest import api_data

@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户管理模块")
class TestUserInfoAPI:
    @allure.story("更新用户昵称接口")
    @allure.title("{title}")
    @pytest.mark.parametrize("title,userId,nickname,success,code,desc,reasonCode,reason,data",api_data["test_update_nickname"])
    @pytest.mark.users
    @pytest.mark.usefixtures("insert_delete_user")
    def test_update_nickname(self,title,userId,nickname,success,code,desc,reasonCode,reason,data,login_fixture):
        logger.info("*************** 开始执行用例 ***************")
        logger.info("发送id：{}，昵称：{}，查看接口返回".format(userId,nickname))
        Authorization = login_fixture['data']['code']
        if title == "更新用户信息_token为空":
            Authorization = None
        elif title == "更新用户信息_token异常":
            Authorization = "jsahdkjahsdjkhaskdh"
        logger.info("获得token:{}".format(Authorization))
        res = user.update_userinfo(Authorization,userId,nickname)
        assert res['success'] == success
        assert res['desc'] == desc
        assert res['code'] == code
        assert res['reasonCode'] == reasonCode
        assert res['reason'] == reason
        if res['code'] == 200:
            assert res['data']['nickname'] == data
        else:
            assert res['data'] == data

        expec_note = "更新昵称成功" if data else "更新昵称失败"
        actul_note = "更新昵称成功" if res['data'] else "更新昵称失败"
        logger.info("期望结果：{}， 实际结果：【 {} 】".format(expec_note, actul_note))
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("查询用户信息接口")
    @allure.title("{title}")
    @pytest.mark.parametrize("title,userId,success,code,desc,reasonCode,reason,data",api_data["test_get_userinfo"])
    @pytest.mark.users
    @pytest.mark.usefixtures("insert_delete_user")
    def test_get_userinfo(self,title,userId,success,code,desc,reasonCode,reason,data,login_fixture):
        logger.info("*************** 开始执行用例 ***************")
        logger.info("发送id：{}，查看接口返回".format(userId))
        Authorization = login_fixture['data']['code']
        if title == "根据用户ID查询用户信息_token为空":
            Authorization = None
        elif title == "根据用户ID查询用户信息_token异常":
            Authorization = "jsahdkjahsdjkhaskdh"
        logger.info("用户token:{}".format(Authorization))
        res = user.get_userinfo(Authorization,userId)
        assert res['success'] == success
        assert res['desc'] == desc
        assert res['code'] == code
        assert res['reasonCode'] == reasonCode
        assert res['reason'] == reason
        if res['code'] == 200:
            assert res['data']['nickname'] == data
        else:
            assert res['data'] == data

        expec_note = "查询用户信息成功" if data else "查询用户信息失败"
        actul_note = "查询用户信息成功" if res['data'] else "查询用户信息失败"
        logger.info("期望结果：{}， 实际结果：【 {} 】".format(expec_note, actul_note))
        logger.info("*************** 结束执行用例 ***************")
if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_07_user_info.py"])