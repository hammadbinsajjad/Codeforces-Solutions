#include <iostream>
#include <vector>
using namespace std;

int main() {
    string s1, s2;
    cin >> s1 >> s2;

    if (s1.length() != s2.length()) {
        cout << "NO" << endl;
        return 0;
    }

    int diffs = 0;
    vector<char> v1, v2;
    for (int i = 0; i < s1.size(); i++) {
        if (s1[i] != s2[i]) {
            diffs += 1;
            v1.push_back(s1[i]);
            v2.push_back(s2[i]);
        }
    }

    if (diffs > 2) {
        cout << "NO" << endl;
        return 0;
    }
    else {
        if (v1[0] == v2[1] && v1[1] == v2[0]) cout << "YES" << endl;
        else cout << "NO" << endl;
    }

}