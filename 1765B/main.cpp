#include <bits/stdc++.h>
using namespace std;

int checkString(string input) {
    int key_hit = 1;
    for (int i = 0; i < input.length(); i++) {
        if (key_hit % 2 == 0) {
            if (input[i] == input[i + 1] && i < input.length() - 1) {
                i++;
            }
            else {
                return 0;
            }
        }
        // else {
        //     if (input[i] == input[i + 1] && i < input.length() - 1){
        //         return 0;
        //     }
        // }
        key_hit++;
    }
    return 1;
}

int main() {
    int t;
    cin >> t;
    vector<int> results(t);

    for (int i = 0; i < t; i++) {
        int length;
        cin >> length;
        string s;
        cin >> s;
        results[i] = checkString(s);
    }

    for (int r:results) {
        if (r)  cout << "YES" << endl;
        else cout << "NO" << endl;
    }
}