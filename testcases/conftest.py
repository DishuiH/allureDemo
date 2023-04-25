"""
整体测试用例前置步骤
"""
import os
import pytest
import allure
from common.logger import logger#日志文件
from common.read_data import data#读yaml文件工具
from api.user import user#user模块接口包
# from common.mysql_operate import db#数据库操作

#加载测试数据
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data
#初始化数据
base_data = get_data("base_data.yml")
#接口测试数据
api_data = get_data("api_test_data.yml")
#流程测试数据
scenario_data = get_data("scenario_test_data.yml")


@pytest.fixture(scope='class')
def get_user_access_token():
    """调用login接口获取key值"""
    username = base_data["api_user"]["username"]
    password = base_data["api_user"]["password"]
    """get_access_token已包含登陆接口login,并拿到username和key传入get_access_token"""
    loginMfa_api = user.get_access_token(username, password)
    logger.info("登录用户：{},密码：{},接口返回：{}".format(username, password, loginMfa_api))
    """从loginMfa_api获取access_token"""
    access_token = loginMfa_api['access_token']
    yield access_token


# @pytest.fixture(scope="class")
# def login_fixture():
#     """所有检测token的接口都需要先登录"""
#     username = base_data["init_admin_user"]["username"]
#     password = base_data["init_admin_user"]["password"]
#     loginInfo = user.email_login(username,password)
#     logger.info("登录用户：{},密码：{},接口返回：{}".format(username, password, loginInfo))
#     yield loginInfo


# @pytest.fixture(scope="class")
# def insert_delete_user():
#     """在数据库插入一条测试用户数据,用例执行后删除刚刚插入的用户数据"""
#     insert_sql = base_data["register_sql"]["insert_delete_user"][0]
#     db.execute_db(insert_sql)
#     logger.info("插入新用户")
#     logger.info("执行前置SQL：{}".format(insert_sql))
#     yield
#     del_sql = base_data["register_sql"]["delete_register_user"]
#     db.execute_db(del_sql)
#     logger.info("删除用户")
#     logger.info("执行后置SQL：{}".format(del_sql))

# @pytest.fixture(scope="class")
# def delete_register_user():
#     """注册用户前，先删除数据，用例执行之后，插入数据"""
#     with allure.step("前置步骤 ==>> 清理数据"):
#         logger.info("注册用户操作：清理用户--准备注册新用户")
#         del_sql = base_data["register_sql"]["delete_register_user"]
#         db.execute_db(del_sql)
#         logger.info("执行前置SQL：{}".format(del_sql))
#     yield
#     with allure.step("后置步骤 ==>> 清理数据"):
#         logger.info("注册用户操作：恢复删除的用户")
#         db.execute_db(del_sql)
#         logger.info("执行后置SQL：{}".format(del_sql))

