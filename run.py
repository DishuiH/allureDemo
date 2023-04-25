"""
可完善点：
1、每执行一次就创一个文件夹，以时间戳命名，不用每次都清空
2、显示environment环境信息(已完成)
3、增加SQL查询验证(已完成)
"""

import pytest
import os
import time


if __name__ == '__main__':
    pytest.main()
    time.sleep(2)
    os.system("copy .\\reports\\environment.properties .\\reports\\temp\\")
    os.system("allure serve ./reports/temp")
