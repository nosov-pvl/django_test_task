import redis
from test_task import settings

def calculate_fibonacci(fro, to):

    fibonacci_list = [0, 1]
    cache = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
    fibonacci_string = cache.get('fibonaccis')
    if fibonacci_string:
        fibonacci_list = [int(x) for x in fibonacci_string.split()]
    last_calculated = len(fibonacci_list)-1
    while to > last_calculated:
        fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
        last_calculated += 1
    cache.set('fibbonaccis', " ".join([str(x) for x in fibonacci_list]))
    return fibonacci_list[fro:to+1]