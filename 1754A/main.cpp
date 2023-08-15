#include <iostream>
#include <stack>

using namespace std;

void solve() {
    int n;
    cin >> n;

    stack<int> s;

    for (int i = 0; i < n; i++) {
        char c;
        cin >> c;
        if (c == 'Q')
            s.push(1);
        else
            if (!s.empty())
                s.pop();
    }

    if (s.empty())
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}