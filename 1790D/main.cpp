#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    map<int, int> cnt;
    set<int> st;

    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        if (cnt.find(arr[i]) == cnt.end()) cnt[arr[i]] = 1;
        else cnt[arr[i]] += 1;

        st.insert(arr[i]);
        st.insert(arr[i] + 1);
    }

    int res = 0;
    int last = 0;
    for (auto el:st) {
        int c = cnt[el];
        res += max(0, c - last);
        last = c;
    }
    cout << res << endl;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    
}