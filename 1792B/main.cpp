#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define vi vector<int>
#define vll vector<long long>
#define map unordered_map
#define fast_io ios::sync_with_stdio(0); cin.tie(0);

void solve() {
    ll a1, a2, a3, a4;
    cin >> a1 >> a2 >> a3 >> a4;
    ll s = a1 + a2 + a3 + a4;

    if (a1) {
        cout << a1 + min(a2, a3) * 2 + min(a1 + 1, abs(a2 - a3) + a4) << endl;
    }
    else {
        cout << 1 << endl;
    }

}

int main() {
    fast_io
    int t; cin >> t;
    while (t--) {
        solve();
    }
}