import threading
import multiprocessing
import time

square_result=[]

def calc_squares(numbers):
    global square_result
    for n in numbers:
        time.sleep(0.5)
        n_sq = n*n
        print('square {} = {} '.format( n, n_sq))
        square_result.append(n_sq)
    print("Square results = ", square_result)



def calc_cubes(numbers):
    for n in numbers:
        time.sleep(0.5)
        print('cube {} = {} '.format(n, n * n * n))


nums = [2,4,6,8]


#Call the functions without multithreading
start_time = time.time()
calc_squares(nums)
calc_cubes(nums)
end_time = time.time()
print ('Total calc time main execution = ', end_time - start_time,square_result)

#Call the functions with multi threading
square_result = []
t1 = threading.Thread(target=calc_squares,args=(nums,))
t2 = threading.Thread(target=calc_cubes,args=(nums,))
start_time = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end_time = time.time()
print ('Total calc time with Multithreading = ', end_time - start_time,square_result)

#Call the functions with multi processes
square_result = []
p1 = multiprocessing.Process(target=calc_squares,args=(nums,))
p2 = multiprocessing.Process(target=calc_cubes,args=(nums,))
start_time = time.time()
p1.start()
p2.start()
p1.join()
p2.join()
end_time = time.time()
print ('Total calc time with Multiprocessing = ', end_time - start_time, square_result)
#Square_result will not be printed with results since in Multi Process the process created has its own address
#space and is not part of the main process address space

#In order to share results in multi process we can use Array, Value Data Types or Queue/Pipes

