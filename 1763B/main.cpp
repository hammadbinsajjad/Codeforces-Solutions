#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define vi vector<int>
#define vll vector<long long>
#define map unordered_map
#define fast_io ios::sync_with_stdio(0); cin.tie(0);
#define rep(s, e, st) for (auto i = s; i < e; i += st)

void solve() {
    int n, k;
    cin >> n >> k;

    int h[n];

    rep(0, n, 1) {
        cin >> h[i];
    }

    pair<int, int> m[n];
    multiset<int> ms;
    rep(0, n, 1) {
        int tp;
        cin >> tp;
        ms.insert(tp);
        m[i] = pair<int, int>{h[i], tp};
    }
    sort(m, m + n);

    rep(0, n, 1) {
        if (k <= 0) {
            cout << "NO" << endl;
            return;
        }
        if (k >= m[i].first) {
            ms.erase(m[i].second);
        }
        else {
            k += k;
            // cout << i << " " << k << endl;
            k -= *ms.begin();
            // cout << i << " " << k << endl;

            i -= 1;
            cout << k << endl;
        }
        // for (auto mt:ms) {
        //     cout << mt << " ";
        // }
        // cout << endl;
    }

    cout << "YES" << endl;

    
}

int main() {
    fast_io
    int t; cin >> t;
    while (t--) {
        solve();
    }
}