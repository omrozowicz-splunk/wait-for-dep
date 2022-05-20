from redis.client import StrictRedis


def check(url):

    try:
        StrictRedis.from_url(url, decode_responses=True)
        return True
    except Exception as e:
        return False
