"""
查询邮箱是否存在接口
"""
import allure
import pytest

from api.user import user
from common.logger import logger
from testcases.conftest import api_data


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户管理模块")
class TestEmailExistAPI:
    @allure.story("查询邮箱是否存在接口")
    @allure.title("{title}")
    @pytest.mark.parametrize("title,email,success,desc,code,reasonCode,reason,data",api_data["test_is_email_exist"])
    @pytest.mark.users
    @pytest.mark.usefixtures("insert_delete_user")
    @allure.step("发送邮箱号进行查询，查看接口返回")
    def test_is_email_exist(self,title,email,success,desc,code,reasonCode,reason,data):
        logger.info("*************** 开始执行用例 ***************")
        logger.info("发送邮箱号：{}，查看接口返回".format(email))
        res = user.is_email_exist(email)
        assert res['success'] == success
        assert res['desc'] == desc
        assert res['code'] == code
        assert res['reasonCode'] == reasonCode
        assert res['reason'] == reason
        assert res['data'] == data

        expec_note = "邮箱存在" if data is True else "邮箱不存在或参数错误"
        actul_note = "邮箱存在" if res['data'] is True else "邮箱不存在或参数错误"
        logger.info("期望结果：{}， 实际结果：【 {} 】".format(expec_note, actul_note))
        logger.info("*************** 结束执行用例 ***************")

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_02_email_exist.py"])