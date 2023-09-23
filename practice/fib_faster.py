def fibonacci_last_three_digits(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 1000

    return b

if __name__ == "__main__":
    numTestCases = int(input())
    results = []

    for i in range(numTestCases):
        n = int(input())
        result = fibonacci_last_three_digits(n)
        results.append(result)

    for result in results:
        print(result)
