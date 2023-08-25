#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, t; cin >> n >> t;

    int arr[n]; for (int i = 0; i < n; i++) cin >> arr[i];

    int l = 0;
    int cur_sum = 0;
    int mc = 0;
    for (int r = 0; r < n; r++) {
        while (cur_sum + arr[r] > t) {
            cur_sum -= arr[l];
            l += 1;
        }
        cur_sum += arr[r];
        mc = max(mc, r - l  + 1);
    }
    cout << mc << endl;
}