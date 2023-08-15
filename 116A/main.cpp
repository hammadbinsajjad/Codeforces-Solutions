#include <bits/stdc++.h>
using namespace std;

int main() {
    int lines;
    cin >> lines;

    int max = 0;
    int current_passengers = 0;
    for (int i = 0; i < lines; i++) {
        int n1, n2;
        cin >> n1 >> n2;
        current_passengers = (current_passengers - n1) + n2;

        if (current_passengers > max) {
            max = current_passengers;
        }
    }

    cout << max << endl;
}