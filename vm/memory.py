from typing import Tuple, Union
import traceback

class Memory:
    def __init__(self, memory_size = None):
        if memory_size is None:
            memory_size = 1000
        self._mem = [0] * memory_size

    def size(self):
        return len(self._mem)

    def resize(self, newsize: int):
        if newsize < len(self._mem):
            print("ERROR: cannot resize memory to be smaller")
        elif newsize == len(self._mem):
            return
        else:
            diff = newsize - len(self._mem)
            self._mem.extend([0] * diff)

    def read(self, location: Union[int, Tuple[int, int]]) -> int:
        loc = location[1] if isinstance(location, tuple) else location

        if loc >= len(self._mem):
            self.resize(loc + 1)

        try:
            return self._mem[loc]
        except IndexError:
            print("Index {} out-of-bounds of list of size {}".format(loc, self.size()))
            traceback.print_exc()
            exit(1)

    def write(self, location: Union[int, Tuple[int, int]], value: int):
        loc = location[1] if isinstance(location, tuple) else location

        if loc >= len(self._mem):
            self.resize(loc + 1)

        self._mem[loc] = value

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._mem[key]
        elif isinstance(key, slice):
            if key.stop > self.size():
                self.resize(key.stop)
            return self._mem[key]
        else:
            print("Unexpected key type: {}".format(key))
            exit(1)
