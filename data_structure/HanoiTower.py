def hanoi(n, a, b, c, target):
    if n == 1:
        print(a, c)
        return

    tmp = 2 ** (n-1)
    if target < tmp:
        hanoi(n-1, a, c, b, target)
    elif tmp == target:
        print(a, c)
    elif target > tmp:
        hanoi(n-1, b, a, c, target - tmp)


if __name__ == "__main__":
    numTestCases = int(input())
    for i in range(numTestCases):
        num_disks, target = map(int, input().split())
        hanoi(num_disks, 1, 2, 3, target)
