#include <stdio.h>

#define MAX_SIZE 1000
void bubbleSort(int a[], int n);
void bubbleSortImproved1(int a[], int n);
void bubbleSortImproved2(int a[], int n);
void copyArray(int a[], int b[], int n);

void swap(int* a, int* b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void copyArray(int a[], int b[], int n){
    for (int i=0; i<n; i++)
        a[i] = b[i];
}

void bubbleSort(int a[], int n) {
    int countCmpOps = 0;
    int countSwaps = 0;

    for (int p = 1; p < n; p++) {
        for (int i = 1; i < n - p + 1; i++) {
            countCmpOps++;
            if (a[i - 1] > a[i]) {
                countSwaps++;
                swap(&a[i-1], &a[i]);
            }
        }
    }

    printf("%d %d ", countCmpOps, countSwaps);
}

void bubbleSortImproved1(int a[], int n) {
    int countCmpOps = 0;
    int countSwaps = 0;

    for (int p = 1; p < n; p++) {
        int swapped = 0;
        for (int i = 1; i < n - p + 1; i++) {
            countCmpOps++;
            if (a[i - 1] > a[i]) {
                countSwaps++;
                swap(&a[i-1], &a[i]);
                swapped = 1;
            }
        }
        if (!swapped) {
            break;
        }
    }

    printf("%d %d ", countCmpOps, countSwaps);
}

void bubbleSortImproved2(int a[], int n) {
    int countCmpOps = 0;
    int countSwaps = 0;
    int lastSwappedPos = n;

    while (lastSwappedPos > 0) {
        int swappedPos = 0;
        for (int i = 1; i < lastSwappedPos; i++) {
            countCmpOps++;
            if (a[i - 1] > a[i]) {
                countSwaps++;
                swap(&a[i-1], &a[i]);
                swappedPos = i;
            }
        }
        lastSwappedPos = swappedPos;
    }

    printf("%d %d ", countCmpOps, countSwaps);
}

int main() {
    int numTestCases;
    scanf("%d", &numTestCases);

    for (int i = 0; i < numTestCases; ++i) {
        int num;
        int a[MAX_SIZE], b[MAX_SIZE];

        scanf("%d", &num);

        for (int j = 0; j < num; j++) {
            scanf("%d", &b[j]);
        }

        copyArray(a, b, num);
        bubbleSort(a, num);

        copyArray(a, b, num);
        bubbleSortImproved1(a, num);

        copyArray(a, b, num);
        bubbleSortImproved2(a, num);
        printf("\n");
    }

    return 0;
}