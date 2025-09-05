def returnValueFunction(n):
    """
    Function to return double the value of n
    Parameter:
        n (int): Input number (1 ≤ n ≤ 5)
    Returns:
        int: Double the value of n
    """
    return n * 2

# Test cases
if __name__ == "__main__":
    # Test with n = 2
    print(returnValueFunction(2))  # Output: 4
    
    # Additional test cases
    print(returnValueFunction(1))  # Output: 2
    print(returnValueFunction(3))  # Output: 6
    print(returnValueFunction(4))  # Output: 8
    print(returnValueFunction(5))  # Output: 10


# https://www.geeksforgeeks.org/dsa/logic-building-problems/