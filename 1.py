from WaimaiSpider.settings import REDIS_URL

import redis

rcon = redis.from_url(REDIS_URL)
a = rcon.llen("proxies")
print(a)
b = rcon.lrange("proxies",0,-1)
print(b)
# c = rcon.lrem("proxies", "27.150.162.56:41514")
# print(a)