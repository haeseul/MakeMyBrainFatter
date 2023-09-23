def main():
    numTestCases = int(input())

    for i in range(numTestCases):
        num = int(input())
        a = list(map(int, input().split()))
        combSort(a)

def combSort(a):
    gap = len(a)
    shrink = 1.3
    sorted = False

    while sorted is False:
        gap = max(1, int(gap / shrink))
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < len(a):
            if a[i] > a[i+gap]:
                a[i], a[i+gap] = a[i+gap], a[i]
                sorted = False
            i += 1
    return a