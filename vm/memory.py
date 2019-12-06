import numpy as np
from typing import Tuple, Union

class Memory:
    def __init__(self):
        self._mem = np.zeros(1000, np.int64)

    def size(self):
        return self._mem.size

    def resize(self, newsize: int):
        np.reshape(self._mem, newsize)

    def read(self, location: Union[int, Tuple[int, int]]) -> int:
        loc = location[1] if isinstance(location, tuple) else location

        if loc > self._mem.size:
            np.reshape(self._mem, loc)

        return self._mem[loc]

    def write(self, location: Union[int, Tuple[int, int]], value: int):
        loc = location[1] if isinstance(location, tuple) else location

        if loc > self._mem.size:
            np.reshape(self._mem, loc)

        self._mem[loc] = value

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._mem[key]
        elif isinstance(key, slice):
            if key.stop > len(self._mem):
                np.reshape(self._mem, key.stop)
            return self._mem[key]
        else:
            print("Unexpected key type: {}".format(key))
            exit(1)
