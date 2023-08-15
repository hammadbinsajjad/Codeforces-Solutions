#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> v(n + 1);
    int temp;
    int distinct = 0;
    for (int i = 0; i < m; i++) {
        cin >> temp;
        if (v[temp] == 0) {
            v[temp] += 1;
            distinct += 1;
        }
        else {
            v[temp]++;
        }

        if (distinct == n) {
            cout << 1;
            for (int &el:v) {
                el--;
                if (el == 0) distinct--;
            }
        }
        else{
            cout << 0;
        }
    }

}