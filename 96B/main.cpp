#include <bits/stdc++.h>
using namespace std;

vector<long long> res;
long long t;
void recurse(long long n, int c4, int c7) {
    if (n > (long long)1e11) return;
    if (c4 == c7 && t <= n) {
        res.push_back(n);
    }
    else {
        n *= 10;
        recurse(n + 4,c4 + 1, c7);
        recurse(n + 7,c4, c7 + 1);
    }
}

int main() {
    cin >> t;
    recurse(0, 0, 0);
    cout << *min_element(res.begin(), res.end()) << endl;
}