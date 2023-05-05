import functools
import threading
import time


class RWLocked:
    def __init__(self):
        self._write_lock = threading.Lock()
        self._read_lock = threading.Lock()
        self._readers = 0


def read_lock(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        with self._read_lock:
            self._readers += 1
            if self._readers == 1:
                self._write_lock.acquire()

        try:
            result = func(self, *args, **kwargs)
        finally:
            with self._read_lock:
                self._readers -= 1
                if self._readers == 0:
                    self._write_lock.release()

        return result

    return wrapper


def write_lock(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self._write_lock.locked():
            self._write_lock.acquire()
            result = func(self, *args, **kwargs)
            self._write_lock.release()
            return result
        else:
            return func(self, *args, **kwargs)

    return wrapper
