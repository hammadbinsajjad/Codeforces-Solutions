#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int test_case = 0; test_case < t; test_case++) {
        int c;
        cin >> c;
        vector<int> v(c);
        int max1 = -1, max2 = -1;
        
        // Input
        for (int i = 0; i < c; i++) {
            cin >> v[i];
            if (v[i] > max1) {
                max2 = max1;
                max1 = v[i];
            }
            else if (v[i] > max2) {
                max2 = v[i];
            }
        }

        // Ouput
        for (int i = 0; i < c; i++) {
            if (v[i] == max1) cout << v[i] - max2 << " ";
            else cout << v[i] - max1 << " ";
        }
        cout << endl;
    }
}