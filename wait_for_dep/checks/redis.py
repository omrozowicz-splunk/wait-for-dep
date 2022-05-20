from redis.client import StrictRedis


def check(url):

    try:
        connection = StrictRedis.from_url(url, decode_responses=True)
        connection.ping()
        return True
    except Exception as e:
        return False
