def calculate_average(numbers):
    total = 0
    # Inefficient loop: iterating with index instead of direct iteration
    for i in range(len(numbers)):
        total += numbers[i]
    # Potential division by zero if numbers is empty
    return total / len(numbers)

def buggy_function(x):
    # Syntax error: using assignment instead of equality comparison
    if x = 10:
        print("x is 10")
    else:
        print("x is not 10")

def inefficient_loop(n):
    result = []
    # Nested loop that could be optimized
    for i in range(n):
        for j in range(n):
            result.append(i * j)
    return result

if __name__ == "__main__":
    # Edge-case: empty list will cause division by zero in calculate_average
    print(calculate_average([1, 2, 3]))
    buggy_function(10)
    print(inefficient_loop(5))