#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

//int a[100001];

//int binarySearch(int num, int start, int end) {
//    int mid = (start + end) / 2;
//
//    if (start <= end) {
//        if (num == a[mid]) {
//            return 1;
//        } else if (num > a[mid]) {
//            return binarySearch(num, mid + 1, end);
//        } else if (num < a[mid]) {
//            return binarySearch(num, start, mid - 1);
//        }
//    }
//    return 0;
//}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int n, m;
    cin >> n;
    
    unordered_map<int, int> map;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        map[temp]++;
    }
    
    cin >> m;

    for (int i = 0; i < m; i++) {
        int x;
        cin >> x;
        if (map[x]) {
            cout << "1\n";
        } else {
            cout << "0\n";
        }
    }

    return 0;
}