"""
本模块测试用例前置步骤
"""

import pytest
from testcases.conftest import api_data

#此函数传入测试用例函数名，获取测试用例测试数据，因为将一个模块的测试数据都放在一个文件里了，这样才好找
@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return api_data.get(testcase_name)