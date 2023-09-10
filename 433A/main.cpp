#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    long long p1 = 0;
    long long p2 = 0;

    int n; cin >> n;

    int arr[n];
    for (int i = 0; i < n; i++) cin >> arr[i];

    sort(arr, arr + n, greater<int>());

    for (int i = 0; i < n; i++) {
        int v = arr[i];
        if (p1 <= p2) p1 += v;
        else p2 += v;
    }

    if (p1 == p2) cout << "YES" << endl;
    else cout << "NO" << endl;
}