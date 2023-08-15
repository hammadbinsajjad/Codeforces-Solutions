#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int findMin(string& s) {
    int min = 0;
    int i = 0;
    for (char c : s) {
        if (c <= s[min]) {
            min = i;
        }
        i++;
    }

    return min;
}

string replaceLetter(string& s) {
    int min = findMin(s);
    string c = s.substr(min, 1);

    // int i = 0;
    // for (i = 0; i < s.length(); i++) {
    //     if (s[i] != c) {
    //         break;
    //     }
    // }

    c += s.substr(0, min);
    c += s.substr(min + 1); 
    return c;
}

void solve() {
    int n;
    cin>>n;
    string s;
    cin >> s;
    cout << replaceLetter(s) << endl;
}

int main() {
    int t;
    cin >> t; 

    while (t--) {
        solve();
    }
}