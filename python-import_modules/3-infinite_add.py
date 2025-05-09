#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = sum(int(arg) for arg in sys.argv[1:]) # Sum all arguments
    print(total) # Print the total
