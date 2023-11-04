def findMinMax(a, low, high, max, min):
    global count_recursive_call
    count_recursive_call += 1

    # 원소가 1개인 경우
    if low == high:
        max, min = a[low], a[high]

    # 원소가 2개인 경우
    elif low+1 == high:
        if a[low] > a[high]:
            max, min = a[low], a[high]
        else:
            max, min = a[high], a[low]
    else:
        mid = (low + high) // 2

        max1, min1 = findMinMax(a, low, mid, max, min)
        max2, min2 = findMinMax(a, mid+1, high, max, min)

        max = max1 if max1 > max2 else max2
        min = min1 if min1 < min2 else min2

    return max, min


if __name__ == '__main__':
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        count_recursive_call = 0
        a = list(map(int, input().split()))
        num = a.pop(0)
        max, min = findMinMax(a, 0, num-1, -1, -1)
        print(max, min, count_recursive_call)