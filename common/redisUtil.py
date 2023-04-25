import redis
from common.get_config import config_data as cfg
import time
import json

class RedisUtil():
    def __init__(self):
        self.host=cfg.get("redis",{}).get("redis_host")
        self.port=cfg.get("redis",{}).get("redis_port")
    def getData(self,key):
        time.sleep(3)
        code = "null"
        try:
            r = redis.StrictRedis(host=self.host, port=self.port, socket_timeout=5)
            code = r.get(key)
        except Exception as e:
            print(e)
        return code

    def getHashData(self,name,key):
        code = "null"
        try:
            pool = redis.ConnectionPool(host=self.host, port=self.port, socket_timeout=5)
            r = redis.StrictRedis(connection_pool=pool)
            bytes_code = r.hget(name=name,key=key)
            if bytes_code:
                str_code = bytes_code.decode('ascii')
                json_code = json.loads(str_code)
                for i in json_code:
                    code = i
                    break
        except Exception as e:
            print(e)
        return code

redis_util = RedisUtil()

if __name__ == '__main__':
    redis_util = RedisUtil()
    name = "timekettle.markov.web.user.defence.code"
    key = "test_01@163.com:register"
    code = redis_util.getHashData(name,key)
    print(code)