#include <bits/stdc++.h>
using namespace std;

int main()
{
    int num1, num2;
    char temp;

    int t;
    cin >> t;
    vector<int> results(t);

    for (int i = 0; i < t; i++)
    {
        cin >> num1;
        // num1 -= 48;

        cin >> temp;

        cin >> num2;
        // num2 -= 48;

        // getchar();
        int res = num1 + num2;
        results[i] = res;
    }

    for (int r:results) {
        cout << r << endl;
    }
    return 0;
}