from collections import OrderedDict

func_name =""
def lru_cache(size): 
    def real_decorator(function):
        print(function.__name__)
        def wrapper(*args,**kwargs):
            global func_name
            global lru_dict
            global capacity 
            if func_name != (function.__name__):
                lru_dict = OrderedDict()
                func_name = function.__name__
                capacity = size
                print(f'Cache initialised with size{capacity}')
            if args in lru_dict:
                val = lru_dict[args]
                lru_dict.move_to_end(args, False)
                print(f'[Cache hit]  {function.__name__}({args}) -> {val}')
                return val
            else:
                val = function(*args,**kwargs)
                if len(lru_dict) >= capacity:
                    lru_dict.popitem()
                lru_dict[args] = val
                lru_dict.move_to_end(args, False)
                print(f'{function.__name__}({args}) -> {val}')
                return val
        return wrapper
    return real_decorator

            