import time
from functools import wraps

def speed_calc_decorator(func):
    @wraps(func)                  #it preserves the metadata of our original functions like add here
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)        # run original function
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        print(f"{func.__name__} took {elapsed:.4f} seconds")
        return result, elapsed                 # return both result & runtime
    return wrapper

# Example usage
@speed_calc_decorator         #(syntactic sugar)
def slow_loop(n):
    for i in range(n):
        i * i

res, runtime = slow_loop(1000000)
print("Result:", res)
print("Time:", runtime)

