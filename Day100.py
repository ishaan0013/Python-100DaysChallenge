def SieveOfEratosthenes(num):
    prime = [True for _ in range(num + 1)]
    # boolean array
    p = 2
    while p**2 <= num:
        if prime[p] == True:
            for i in range(p**2, num + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, num + 1):
        if prime[p]:
            print(p)


if __name__ == "__main__":
    num = int(input("Enter Number:\n"))
    print("Following are the prime numbers smaller"),
    print("than or equal to", num)
    SieveOfEratosthenes(num)
