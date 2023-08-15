#include <iostream>
#include <vector>

#define ll long long
#define rep(x) for (int i = 0; i < x; i++)

using namespace std;

int main() {
    int n; cin >> n;

    int f = 0;
    rep(n) {
        int t;
        cin >> t;
        f += t; 
    }

    int c = 0;
    rep(5) {
        if ((f + i + 1) % (n + 1) != 1) {
            c += 1;    
        }
    }
    cout << c << endl;
    
}