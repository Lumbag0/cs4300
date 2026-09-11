def is_negative(x: int | float) -> bool:
    var_negative = False

    # negative times a positive is always negative
    if (x * 1) < 0:
        var_negative = True
    
    return var_negative

def is_zero(x: int | float) -> bool:
    var_zero = False

    if x == 0:
        var_zero = True
    return var_zero

def first_10_prime() -> list:
    primes_found = 0
    primes = []
    num = 2
    
    for num in range(2, 100):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        if len(primes) == 10:
            break        
    return primes

def sum_to_100() -> int:
    num = 0
    total = 0
    while num < 100:
        total = total + num
        num = num + 1
        total = total + 1
    return total

def main():
    print("-"*50)
    print("Negative Check")
    print("-"*50)
    num=1
    print(f"Is {num} a negative? -- {is_negative(num)}")

    num = -1
    print(f"Is {num} a negative? -- {is_negative(num)}")

    print("-"*50)
    print("Zero Check")
    print("-"*50)
    print(f"Is {num} zero? -- {is_zero(num)}")
    num = 0
    print(f"Is {num} zero? -- {is_zero(num)}")

    print("-"*50)
    print("First 10 Prime Numbers")
    print("-"*50)
    primes = first_10_prime()
    for i in primes:
        print(i)

    print("-" * 50)
    print("Sum To 100")
    print("-"*50)
    print(sum_to_100())

if __name__ == "__main__":
    main()