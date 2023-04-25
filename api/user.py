"""
邮箱注册接口：email_register
邮箱是否存在接口：is_email_exist
获取验证码接口：get_verify_code
验证验证码接口：verify_code
邮箱登录接口：email_login
忘记密码：reset_pass
微信登录：wechat_login
谷歌登录：google_login
脸书登录：facebook_login
苹果登录：apple_login
更新用户信息：update_userinfo
获取用户信息:get_userinfo
"""
import time

from core.rest_client import RestClient
from common.get_config import api_root_url
from common.logger import logger


class User(RestClient):
    def __init__(self, root_url, **kwargs):
        super(User, self).__init__(root_url, **kwargs)

    def email_login(self, username, password, logintype):
        """请求的siteKey为当前13位时间戳"""
        site_key = round(time.time()*1000)
        headers = {
            "Content-Type": "application/json",
        }
        json = {
          "userIdOrEmail": username,
          "loginType": logintype,
          "password": password,
          "captcha": "",
          "siteKey": site_key
        }

        res = self.post('/api/v2/public/auth/login', json=json, headers=headers)
        res_info = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.json())
        logger.info(res_info)
        return res

    def sms_login(self, phoneNumber, password, logintype):
        """请求的siteKey为当前时间的13位时间戳"""
        site_key = round(time.time()*1000)
        headers = {
            "Content-Type": "application/json",
        }
        json = {
          "phoneNumber": phoneNumber,
          "loginType": logintype,
          "password": password,
          "captcha": "",
          "siteKey": site_key
        }

        res = self.post('/api/v2/public/auth/login', json=json, headers=headers)
        res_info = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.json())
        logger.info(res_info)
        return res

    def get_access_token(self, email, password):
        """请求的siteKey为当前13位时间戳"""
        login_res = self.email_login(email,password)
        key = login_res['key']
        username = login_res['user']
        headers = {
            "Content-Type": "application/json",
        }
        json = {
          "user": username,
          "key": key
        }
        res = self.post('/api/v2/public/auth/loginMfa', json=json, headers=headers)
        res_info = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.json())
        logger.info(res_info)
        return res.json()

    def get_userinfo(self,Authorization,userId):
        headers = {
            "Authorization": Authorization,
        }
        params = {
            "userId": userId
        }
        res = self.get('/user/userInfo/getUserById',params=params,headers=headers)
        res_info = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.json())
        logger.info(res_info)
        return res.json()

    def admin_login(self, username, password):
        """请求的siteKey为当前13位时间戳"""
        site_key = round(time.time()*1000)
        headers = {
            "Content-Type": "application/json",
            "captcha":
            "reqTime": site_key
        }
        json = {"user": username,
                "password": password,
                "rememberMe": "false",
                "captcha": "whatever",
                "siteKey": site_key
                }

        res = self.post('/api/v1/public/admin/auth/login', json=json, headers=headers)
        res_info = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.json())
        logger.info(res_info)
        return res.json()

    def get_admin_access_token(self, email, password):
        """请求的siteKey为当前13位时间戳"""
        login_res = self.admin_login(email, password)
        key = login_res['key']
        username = login_res['user']
        headers = {
            "Content-Type": "application/json",
        }
        json = {"code":"",
                "user": username,
                "key": key,
                "totp": 'true'
        }
        res = self.post('/api/v1/public/admin/auth/loginMfa', json=json, headers=headers)
        res_info = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.status_code, res.json())
        logger.info(res_info)
        return res.json()

user = User(api_root_url)

if __name__ == '__main__':
    print(user.email_login("shawn.xiao2",'P@ssw0rd').status_code)
