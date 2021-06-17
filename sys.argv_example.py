#!/usr/bin/env python3

"""
Simple command-line tool using sys.argv
"""

try:
    import sys

    if __name__ == "__main__":
        print(f"The first argument: '{sys.argv[0]}'")
        print(f"The second argument: '{sys.argv[1]}'")
        print(f"The third argument: '{sys.argv[2]}'")
        print(f"The fourth argument: '{sys.argv[3]}'")
except:
    print("example: ./sys.argv_example.py --a-flag some-value 13")
