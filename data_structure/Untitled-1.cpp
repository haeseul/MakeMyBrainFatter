#include <iostream>
#include <vector>

using namespace std;

void swap(int* a, int* b){
    
}

void bubbleSort(vector<int>& a, int n) {
    int countCmpOps = 0; // 비교 연산자 실행 횟수
    int countSwaps = 0;  // swap 함수 실행 횟수

    for (int p = 1; p < n; ++p) {
        for (int i = 1; i < n - p + 1; ++i) {
            ++countCmpOps;
            if (a[i - 1] > a[i]) {
                ++countSwaps;
                swap(a[i - 1], a[i]);
            }
        }
    }

    cout << countCmpOps << " " << countSwaps << " ";
}

void bubbleSortImproved1(vector<int>& a, int n) {
    int countCmpOps = 0; // 비교 연산자 실행 횟수
    int countSwaps = 0;  // swap 함수 실행 횟수

    for (int p = 1; p < n; ++p) {
        bool swapped = false;
        for (int i = 1; i < n - p + 1; ++i) {
            ++countCmpOps;
            if (a[i - 1] > a[i]) {
                ++countSwaps;
                swap(a[i - 1], a[i]);
                swapped = true;
            }
        }
        if (!swapped) {
            break;
        }
    }

    cout << countCmpOps << " " << countSwaps << " ";
}

void bubbleSortImproved2(vector<int>& a, int n) {
    int countCmpOps = 0; // 비교 연산자 실행 횟수
    int countSwaps = 0;  // swap 함수 실행 횟수
    int lastSwappedPos = n;

    while (lastSwappedPos > 0) {
        int swappedPos = 0;
        for (int i = 1; i < lastSwappedPos; ++i) {
            ++countCmpOps;
            if (a[i - 1] > a[i]) {
                ++countSwaps;
                swap(a[i - 1], a[i]);
                swappedPos = i;
            }
        }
        lastSwappedPos = swappedPos;
    }

    cout << countCmpOps << " " << countSwaps << " ";
}

int main() {
    int numTestCases;
    cin >> numTestCases;

    for (int i = 0; i < numTestCases; ++i) {
        int num;
        cin >> num;
        vector<int> b(num);
        for (int j = 0; j < num; ++j) {
            cin >> b[j];
        }

        bubbleSort(b, num);
        bubbleSortImproved1(b, num);
        bubbleSortImproved2(b, num);

        cout << endl;
    }

    return 0;
}
