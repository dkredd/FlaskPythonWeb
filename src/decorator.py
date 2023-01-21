import time
import functools

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        start_time = time.time()
        result = func(*args, **kargs)
        end_time = time.time()
        print("function {} executed in {} time",func.__name__,(end_time-start_time))
        return result
    return wrapper

@timeit
def calc_squares(nums):
    result = []
    for n in nums:
        result.append(n*n)
    return result

@timeit
def calc_cubes(nums):
    result = []
    for n in nums:
        result.append(n*n*n)
    return result

nums = range(1,100)
result1 = calc_squares(nums)
result2 = calc_cubes(nums)
print(result1,"\n\n")
print(result2)
print(calc_cubes.__name__)