import time


def cache(duration):
    def cache_inner(function):
        memo = {}
        tick = {}

        def wrapper(*args):
            if string_args(*args) in memo and int(time.time()) - tick.get(string_args(*args), 0) < duration:
                return memo[string_args(*args)]
            else:
                rv = function(*args)
                memo[string_args(*args)] = rv
                tick[string_args(*args)] = int(time.time())
                return rv

        return wrapper

    return cache_inner


def string_args(*args):
    if len(args) == 0:
        return "cache"
    return "-".join([str(s) for s in args])
