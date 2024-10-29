import time
import threading
import requests

def readExample():
    response = requests.get("https://nalindeepan007.github.io/CVissfolio/")
    print(f"status code => {response.status_code} \n")

thread1 = threading.Thread(target=readExample)
thread2 = threading.Thread(target=readExample)

threadStart = time.time()
thread1.start()
thread2.start()
print("All threads running")
thread1.join()
thread2.join()
threadEnd = time.time()
print(f'time taken => {threadEnd - threadStart:.4f} seconds')

# multi threading in Python
# GIL is released in I/O operations
# so threads do concurrent work during I/O operations but not for CPU bound tasks
# some exceptions are there where we can release GIL for CPU bound tasks