import multiprocessing
import time

#Function to test lock
def deposit(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


balance = multiprocessing.Value('i',200)
lock = multiprocessing.Lock()
p1 = multiprocessing.Process(target=deposit, args=(balance,lock))
p2 = multiprocessing.Process(target=withdraw, args=(balance,lock))


p1.start()
p2.start()

p1.join()
p2.join()

print("Balance Ending = ", balance.value)


#Functions that use and time Pool
def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

t1= time.time()
p = multiprocessing.Pool()
result = p.map(f,range(10000))
p.close()
p.join()
t2= time.time()
print("pool took time = ",t2-t1 )
#print("result=",result)

result = []
t1= time.time()
for i in range(10000):
    result.append(f(i))
t2= time.time()
print("Serial took time = ",t2-t1 )

