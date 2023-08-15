#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, b;
    cin >> n >> b;
    vector<int> v(n);
    vector<int> cuts;

    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    int even = 0, odd = 0, temp, cut = 0;
    for (int i = 0; i < n - 1; i++) {
        if (v[i] % 2 == 0) even++;
        else odd++;

        if (even == odd) {
            cuts.push_back(abs(v[i] - v[i + 1]));
        }
    }

    sort(cuts.begin(), cuts.end());
    
    for (int c:cuts) {
        if (c <= b) {
            cut++;
            b -= c;
        }
        else break;
    }
    cout << cut << endl;
}