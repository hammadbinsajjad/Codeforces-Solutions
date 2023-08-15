#include <iostream>
#include <vector>

using namespace std;

int main() {
    long long n; cin >> n;

    vector<long long> arr(n);
    for (long long i = 0; i < n; i++) {
        cin >> arr[i];
    }

    vector<long long> dp_forward(n);
    vector<long long> dp_backward(n);

    for (long long i = 0; i < n; i++) {
        dp_forward[arr[i] - 1] = i + 1;
    }

    for (long long i = n - 1, j = 0; i >= 0; i--, j++) {
        dp_backward[arr[i] - 1] = j + 1;
    }

    long long m; cin >> m;

    long long sum_for = 0;
    long long sum_back = 0;
    long long t;
    for (long long i = 0; i < m; i++) {
        cin >> t;
        sum_for += dp_forward[t - 1];
        sum_back += dp_backward[t - 1];
    }

    cout << sum_for << " " << sum_back << endl;

}
