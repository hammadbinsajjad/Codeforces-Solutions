#include <iostream>
#include <vector>
using namespace std;

int count;
void makeSeqs(int n, string s, int l, int r) {
    if (count == n) return;
    if (s.length() == 2*n) {
        cout << s << endl;
        count += 1;
    }
    else {
        if (l < n) makeSeqs(n, s + '(', l + 1, r);
        if (r < l) makeSeqs(n, s + ')', l, r + 1);
    }
}

int main() {
    int t; cin >> t;
    while (t--) {
        int n;
        cin >> n;
        count = 0;
        makeSeqs(n, string(), 0, 0);
    }
}