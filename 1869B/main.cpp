#include <iostream>
#include <vector>
#include <utility>
#include <cmath>
#include <algorithm>
using namespace std;

#define ll long long

ll dist(ll x1, ll y1, ll x2, ll y2) {
    return abs(x1-y1) + abs(x2-y2);
}

void solve() {
    ll n, k, a, b;
    cin >> n >> k >> a >> b;

    pair<ll, ll>s, e;

    vector<pair<ll, ll>> major(k);
    vector<pair<ll, ll>> simple(n - k);

    for (ll i = 0; i < k; i++) {
        ll x, y;
        cin >> x >> y;
        major[i] = pair<ll, ll>{x, y};

        if (i == a - 1) {
            s = pair<ll, ll>{x, y};
        }
        if (i == b - 1) {
            e = pair<ll, ll>{x, y};
        }
    }

    for (int i = 0; i < n - k; i++) {
        ll x, y;
        cin >> x >> y;
        simple[i] = pair<ll, ll>{x, y};

        if (i + k == a - 1) {
            s = pair<ll, ll>{x, y};
        }
        if (i + k == b - 1) {
            e = pair<ll, ll>{x, y};
        }

    }

    if (k) {
        ll min_major_s = 1e10, min_major_e = 1e10;

        for (auto c:major) {
            min_major_s = min(min_major_s, dist(s.first, c.first, s.second, c.second));
            min_major_e = min(min_major_e, dist(e.first, c.first, e.second, c.second));
        }

        cout << min(dist(s.first, e.first, s.second, e.second), min_major_e + min_major_s) << endl;
    }
    else {
        cout << dist(s.first, e.first, s.second, e.second) << endl;
    }

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;

    while(t--) {
        solve();
    }
}
