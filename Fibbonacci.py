import sys

def fibonacci(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

if __name__ == "__main__":
    print(fibonacci(sys.argv[1]))