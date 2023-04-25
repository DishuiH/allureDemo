"""
测试报告的一些应用函数
"""

import allure

class Report:
    @allure.step("测试步骤")
    def step(self,step_name):
        logger.info("步骤名 ==>> {}".format(step_name))