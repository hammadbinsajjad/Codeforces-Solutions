#include <iostream>
#include <vector>
using namespace std;

bool checkB(vector<int> &b) {
    int v = b[0];

    for (int i = 1; i < b.size(); i++) {
        v = v xor b[i];
    }

    return !v;
}

void solve() {
    int n;
    cin >> n;

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    vector<int> b(n);

    for (int i = 0; i < 256; i++) {
        for (int j = 0; j < n; j++) {
            b[j] = a[j] xor i;
        }

        if (checkB(b)) {
            cout << i << endl;
            return;
        };
    }
    cout << -1 << endl;

}

int main() {
    int t;
    cin >> t;

    while (t--) {
        solve();
    }
}