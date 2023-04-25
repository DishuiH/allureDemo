"""
config可以当作环境变量使用
"""
import os
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

config_path = os.path.join(BASE_PATH, "config", "sit_setting.ini")
config_data = data.load_ini(config_path)
api_root_url = config_data['host']['api_root_url']



