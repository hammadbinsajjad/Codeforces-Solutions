#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

bool isVowel(char c)
{
    char vowels[] = {'a', 'e', 'i', 'o', 'u', 'y'};

    for (char v : vowels)
    {
        if (c == v)
            return true;
    }
    return false;
}

void solve()
{

    string s;

    cin >> s;

    int cons_count = 0;

    for (char c : s)
    {
        if (isVowel(c))
        {
            if (cons_count >= 4)
            {
                cout << "Difficult" << endl;
                return;
            }
            cons_count = 0;
        }
        else
        {
            cons_count++;
        }
    }

    if (cons_count >= 4)
    {
        cout << "Difficult" << endl;
        return;
    }
    cout << "Easy" << endl;
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        solve();
    }
}