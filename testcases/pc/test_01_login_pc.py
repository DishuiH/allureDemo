"""
测试PC端时空壶登录接口demo,后续会不断完善结构
"""
import pytest
import allure

from core.rest_client import RestClient
from common.logger import logger
from testcases.api_test.conftest import api_data



@allure.step("步骤1：登录用户名和密码")
def step_1(username,password):
    logger.info("登录用户名：{},密码：{}".format(username,password))

@allure.severity(allure.severity_level.NORMAL)
@allure.epic("时空壶PC端用户系统")
@allure.feature("用户管理模块")
class TestUserLogin:
    @allure.story("用户登录")
    @allure.description("该用例是针对获取用户登录接口的测试")
    @allure.issue("bug链接", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("用例链接", name="点击，跳转到对应用例的链接地址")
    @allure.title("{title}")
    @pytest.mark.pc
    @pytest.mark.parametrize("title,email,password,expec_res,expec_code,expec_desc",api_data["test_pc_user_login"])
    #函数名要跟yml文件里的key一致
    def test_user_login(self,title,email,password,expec_res,expec_code,expec_desc):
        logger.info("*************** 开始执行用例 ***************")
        api_root_url = "https://live.wttwo.com"
        re = RestClient(api_root_url)
        params = {
            "email":email,
            "password":password
        }
        step_1(email,password)
        res = re.get('/pc/api_test/login',params=params).json()
        #检查点
        assert res['success'] == expec_res
        assert res['code'] == expec_code
        assert res['desc'] == expec_desc
        logger.info("*************** 结束执行用例 ***************")



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_login_pc.py"])
