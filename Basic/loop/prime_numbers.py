# Method 1: Basic approach
def print_primes_basic(start, end):
    print(f"\nPrime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if num > 1:  # Numbers less than 2 are not prime
            for i in range(2, num):
                if num % i == 0:
                    break
            else:  # This else belongs to for loop, executes when no break occurs
                print(num, end=" ")
    print()

# Method 2: More efficient approach using square root
def is_prime(n):
    if n < 2:
        return False
    # Only need to check up to square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_efficient(start, end):
    print(f"\nPrime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
    print()

# Method 3: Most efficient approach using Sieve of Eratosthenes
def print_primes_sieve(start, end):
    # Create a boolean array "is_prime[0..end]" and initialize
    # all entries it as true
    is_prime = [True] * (end + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(end ** 0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i
            for j in range(i * i, end + 1, i):
                is_prime[j] = False

    print(f"\nPrime numbers between {start} and {end} are:")
    for i in range(start, end + 1):
        if is_prime[i]:
            print(i, end=" ")
    print()

# Test all methods
if __name__ == "__main__":
    # Get range from user
    try:
        start = int(input("Enter the start of range: "))
        end = int(input("Enter the end of range: "))
        
        if start > end:
            print("Start should be less than end")
        else:
            # Using basic approach
            print_primes_basic(start, end)
            
            # Using efficient approach
            print_primes_efficient(start, end)
            
            # Using Sieve of Eratosthenes
            print_primes_sieve(start, end)
            
    except ValueError:
        print("Please enter valid integers")

"""
Example output for range 1 to 20:
Prime numbers between 1 and 20 are:
2 3 5 7 11 13 17 19

How it works:
1. A prime number is only divisible by 1 and itself
2. We check each number in the range
3. For each number, we check if it has any divisors
4. If no divisors are found, it's prime
"""
