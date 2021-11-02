import sys

def Euclid_Algori(a, b):
    while b != 0:
        t = b 
        b = a % b
        a = t
    return a

print(Euclid_Algori(60, 12))
'''
if __name__ == "__main__":
    great_divisor = Euclid_Algori(int(sys.argv[1]), int(sys.argv[2]))
    print(great_divisor)
'''