import time
from contextlib import contextmanager
from typing import Optional


@contextmanager
def timer(message: Optional[str] = None):
    if message:
        print(message, end=": ")
    start_time = time.perf_counter()
    yield
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"{elapsed_time:.3f} seconds")
