#include <iostream>
#include <string>
#include <unordered_map>
#include <cmath>

using namespace std;

unordered_map<char, pair<int, int>> m;

void solve() {
    string s;

    pair<int, int> pos(0, 0);

    cin >> s;
    for (char c:s) {
        pos.first += m[c].first;
        pos.second += m[c].second;
    }

    int result = abs(pos.first) + abs(pos.second);
    cout << result << endl;

}

int main() {

    m['U'] = pair<int, int>(0, 1);
    m['D'] = pair<int, int>(0, -1);
    m['L'] = pair<int, int>(-1, 0);
    m['R'] = pair<int, int>(1, 0);

    int t;
    cin >> t;
    while (t--) solve();
}