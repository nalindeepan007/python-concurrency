import functools
import time
from typing import Callable, Any
import asyncio

def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'starting {func} with {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'finished {func} in {total:.4f} second(s)')
        return wrapped
    return wrapper

@async_timed()
async def delay(delaySeconds: int):
    print(f'sleeping for {delaySeconds} seconds')
    await asyncio.sleep(delaySeconds)
    print(f'finished sleeping for {delaySeconds} seconds')
    return delaySeconds

@async_timed()
async def main():
    task1 = asyncio.create_task(delay(2))
    task2 = asyncio.create_task(delay(3))
    await task1
    await task2

asyncio.run(main())

