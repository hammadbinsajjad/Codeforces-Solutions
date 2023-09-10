#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n; cin >> n;

    int l[n];
    int r[n];

    int i = 0;
    while (i < n) {
        cin >> l[i] >> r[i];
        i += 1;
    }

    int ml = *min_element(l, l + n);
    int mr = *max_element(r, r + n);

    for (int i = 0; i < n; i++) {
        if (r[i] == mr && ml == l[i]) {
            cout << i + 1 << endl;
            return 0;
        }
    }
    cout << -1 << endl;
    return 0;
}