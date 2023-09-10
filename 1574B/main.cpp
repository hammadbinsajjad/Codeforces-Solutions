#include <iostream>
using namespace std;

void solve() {
    int a, b, c, m; cin >> a >> b >> c >> m;

    int mx = a + b + c - 3;
    int mn = max(a, max(b, c)) * 2 - a - b - c - 1;

    if (m >= mn && m <= mx) cout << "YES" << endl;
    else cout << "NO" << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}