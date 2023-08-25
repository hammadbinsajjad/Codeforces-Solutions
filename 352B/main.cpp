#include <bits/stdc++.h>
using namespace std;
int main() {
    unordered_map<int, pair<int, int>> m;

    int n; cin >> n;
    
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;

        if (m.find(t) != m.end()) {
            if (m[t].second == -1) continue;
            if (m[t].second == 0) {
                m[t].second = i - m[t].first;
                m[t].first = i;
            }
            else {
                if (i - m[t].first != m[t].second) {
                    m[t].second = -1;
                }
                else {
                    m[t].first = i;
                }
            }
        }
        else {
            m[t] = pair<int, int>{i, 0};
        }
    }
    vector<pair<int, pair<int, int>>> res;
    for (auto v:m) {
        res.push_back(v);
    }

    sort(res.begin(), res.end());
    
    int c = 0;
    for (auto v:res) {
        if (v.second.second != - 1) c += 1; 
    }
    cout << c << endl;
    for (auto v:res) {
        if (v.second.second == -1) continue;
        cout << v.first << " " << v.second.second << endl;
    }

}