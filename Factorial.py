import sys

def factorial_iter(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result

print(factorial_iter(4))
if __name__ == "__main__":
    print(factorial_iter(sys.argv[1]))