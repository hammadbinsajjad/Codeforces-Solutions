#include <bits/stdc++.h>
using namespace std;

int main() {
    stack<char, vector<char>> s;

    string str;

    cin >> str;

    char c;
    int i = 0;
    while (i < str.length()) {
        c = str[i];
        if (c == '\n' || c == ' ' || c == '\0') break;
        if (isalpha(c)) {
            // check if top is that alphabet
            if (!s.empty() && s.top() == c) {
                s.pop();
            }
            else {
                s.push(c);
            }
        }
        else {
            break;
        }
        i++;
    }

    vector<char> results(s.size());

    i = s.size() - 1;
    while(!s.empty()) {
        results[i] = s.top();
        s.pop();
        i--;
    }

    for (char r:results)
    {
        cout << r;
    }

    return 0;
}