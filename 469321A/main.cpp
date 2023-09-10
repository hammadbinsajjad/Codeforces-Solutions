#include <iostream>
using namespace std;

int main() {
    int n, s; cin >> n >> s;

    int c = 0;
    while (s > n) {
        s -= n;
        c += 1;
    }

    if (s != 0) c += 1;
    cout << c << endl;
}