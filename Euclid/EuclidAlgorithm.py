# Euclid Algorithm
# a = q * b + r

def euclid(a,b):
    while True:
        q = a/b
        r = a%b
        if r == 0:
            break
        elif r == 1:
            return r
            break
        else:
            a = b
            b = r

    return b

def main():
    a, b = input("Please enter two integers to find the greatest common divisor: ").split()
    a = int(a)
    b = int(b)

    result = euclid(a,b)
    print(f"The greatest common divisor is {result}")

if __name__ == "__main__":
    main()