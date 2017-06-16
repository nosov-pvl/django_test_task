from django.core.cache import cache


def calculate_fibonacci(fro, to):

    fibonacci_list = [0, 1]
    fibonacci_cached = cache.get('fibonaccis')
    if fibonacci_cached:
        fibonacci_list = fibonacci_cached
    last_calculated = len(fibonacci_list)-1
    while to > last_calculated:
        fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
        last_calculated += 1
    cache.set('fibonaccis', fibonacci_list)
    return fibonacci_list[fro:to+1]
