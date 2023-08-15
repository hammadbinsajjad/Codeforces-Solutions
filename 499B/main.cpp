#include <bits/stdc++.h>
using namespace std;

int main() {
    int n,m;
    cin >> n >> m;

    map<string, string> words;

    string s1, s2;
    for (int i = 0; i < m; i++) {
        cin >> s1 >> s2;
        if (s2.length() < s1.length())
            words[s1] = s2;
        else 
            words[s1] = s1;
    }

    // using s1 here as well
    for (int i = 0; i < n; i++) {
        cin >> s1;
        cout << words[s1] << " ";
    }
    return 0;
}