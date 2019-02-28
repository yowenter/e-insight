GLOBAL_CACHE = {}



def cache(name, expires):
    def inner(f):
        def decorator(*args, **kwargs):
            print(*args, **kwargs)
            return f(*args, **kwargs)
        print(f)
        return decorator
    print(name, expires)
    return inner
