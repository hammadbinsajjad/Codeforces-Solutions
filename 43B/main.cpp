#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <cstring>

using namespace std;

void f(string s, map<char, int>& counts) {
    for (char c:s) {
        if (!isalpha(c)) continue;
        if (counts.find(c) != counts.end()) {
            counts[c]++;
        }
        else {
            counts[c] = 1;
        }
    }
}

int main() {
    string s1;
    getline(cin, s1);

    string s2;
    getline(cin, s2);

    map<char, int> counts_1;
    map<char, int> counts_2;

    f(s1, counts_1);
    f(s2, counts_2);

    for (auto el:counts_2) {
        if (counts_1.find(el.first) != counts_1.end() && counts_1[el.first] >= el.second) continue;
        else {
            cout << "NO" << endl;
            return 0;
        }
    }
    cout << "YES" << endl;

}