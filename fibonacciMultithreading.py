import threading
import time


def printFib(number: int):
    def fib(n: int):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else: 
            return fib(n - 1) + fib(n-2)
    print(f'fib of {number} is {fib(number)}')

def fibsWithThreads():
    firstInputThread = threading.Thread(target=printFib, args=(40,))
    secondInputThread = threading.Thread(target=printFib, args=(41,))
    firstInputThread.start()
    secondInputThread.start()
    firstInputThread.join()
    secondInputThread.join()

startTime = time.time()
fibsWithThreads()
endTime = time.time()
print(f'time taken with multi threading is {endTime-startTime:.4f} seconds')