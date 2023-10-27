def find(a, n):
    max = 1
    j = 1
    if n == 1:
        return a[0]
    else:
        for i in range(n-1):
            if a[i] <= a[i+1]:
                j += 1
                if j >= max:
                    max = j
            else:
                j = 1
        return max

if __name__ == '__main__':
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        a = list(map(int, input().split()))
        num = a.pop(0)
        print(find(a, num))

