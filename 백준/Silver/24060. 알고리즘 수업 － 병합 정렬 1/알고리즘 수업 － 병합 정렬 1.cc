#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int> &A, int p, int q , int r, int k, int &cnt){
    int i = p, j = q + 1, t = 1;
    int temp[r + 2];
    while (i <= q && j <= r) {
        if (A[i] <= A[j]) {
            temp[t++] = A[i++];
        } else {
            temp[t++] = A[j++];
        }
    }

    while (i <= q) {
        temp[t++] = A[i++];
    }

    while (j <= r) {
        temp[t++] = A[j++];
    }

    i = p;
    t = 1;
    while (i <= r) {
        A[i++] = temp[t++];
        if (++cnt == k) {
            cout << temp[t - 1] << "\n";
        }
    }
}

void merge_sort(vector<int> &A, int p, int r, int k, int &cnt) {
    if (p < r) {
        int q = (p + r) / 2;
        merge_sort(A, p, q, k, cnt);
        merge_sort(A, q + 1, r, k, cnt);
        merge(A, p, q, r, k, cnt);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n, k; // n = 배열의 크기, k = 저장 횟수
    cin >> n >> k;

    vector<int> A(n, 0);
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    int q = (n - 1) / 2;
    int cnt = 0;
    merge_sort(A, 0, n - 1, k, cnt);

    if (cnt < k) {
        cout << -1 << "\n";
    }
}