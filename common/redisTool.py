import redis
import json
import sys

def RedisUtil(envir,user_type,email):

    ip = {"dev":"192.168.0.115","uat":"47.245.57.28"}
    p = {"dev":"6379","uat":"32000"}
    type = {"register":"lvtrans.web.user.code:Register","resetPass":"lvtrans.web.user.code:ResetPass","ForgetResetPass":"lvtrans.web.user.code:ForgetResetPass"}

    host = ip[envir]
    port = p[envir]
    name = type[user_type]
    key = email

    code = "null"
    try:
        pool = redis.ConnectionPool(host=host, port=port, socket_timeout=10)
        r = redis.StrictRedis(connection_pool=pool)
        bytes_code = r.hget(name=name,key=key)
        if bytes_code:
            str_code = bytes_code.decode('ascii')
            json_code = json.loads(str_code)
            lenth = len(json_code) - 1
            code = json_code[lenth]['verifyCode']
    except Exception as e:
        print(e)
    return code



if __name__ == '__main__':

    code = RedisUtil(sys.argv[1],sys.argv[2],sys.argv[3])
    print(code)