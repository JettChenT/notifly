import redis
import hashlib

class Updater(object):
    def __init__(self):
        self.red = redis.Redis()
        self.quename = "notifications"
    def add_notification(self,msg:str):
        hash = hashlib.sha1(msg.encode()).hexdigest()
        self.red.lpush(self.quename, hash)
        self.red.hset(hash,"msg",msg)
    def get_notification(self,n_cnt:int=20):
        h_list = self.red.lrange(self.quename, 0, n_cnt)
        res = []
        for hsh in h_list:
            msg = self.red.hget(hsh,"msg")
            res.append(msg)
        return res