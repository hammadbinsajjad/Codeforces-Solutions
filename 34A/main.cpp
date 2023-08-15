#include <iostream>
using namespace std;

#define ll long long
#define vi vector<int>
#define rep(s, e, st) for (int i = s; i < e; i += st)

int main() {
    int n; cin >> n;

    int arr[n];

    rep(0, n, 1){
        cin >> arr[i];
    }

    int min_diff = 2e3;
    int min_index_1;
    int min_index_2;

    rep(1, n, 1) {
        int diff = abs(arr[i] - arr[i - 1]);
        if (diff < min_diff) {
            min_diff = diff;
            min_index_1 = i;
            min_index_2 = i - 1;
        }
    }

    if (abs(arr[0] - arr[n - 1]) < min_diff) {
        cout << 1 << ' ' << n << endl;
    }
    else {
        cout << min_index_1 + 1 << ' ' << min_index_2 + 1 << endl;
    }
}
