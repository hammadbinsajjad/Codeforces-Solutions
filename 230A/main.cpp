#include <bits/stdc++.h>
using namespace std;

int main() {
    int power, n;
    cin >> power >> n;

    vector<pair<int, int>> dragons(n);
    
    // Take input
    for (int i = 0; i < n; i++) {
        cin >> dragons[i].first >> dragons[i].second;
    }

    // Sort so that min power dragon is at top
    sort(dragons.begin(), dragons.end());

    for (int i = 0; i < n; i++) {
        if (power > dragons[i].first) {
            power += dragons[i].second;
        }
        else {
            cout << "NO" << endl;
            return 0;
        }
    }
    cout << "YES" << endl;
    return 0;
}