import sys
from typing import List

def read_input() -> List[str]:
    if len(sys.argv) < 2:
        print("Usage: %s <input filename>" % sys.argv[0])
        exit(1)
    
    filename = sys.argv[1]

    try:
        with open(filename, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print("File %s does not exist!" % filename)
        exit(2)
    except IOError:
        print("Unable to read file %s" % filename)
        exit(3)