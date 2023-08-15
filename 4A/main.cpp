#include <iostream>
using namespace std;

int main() {
    int weight;
    cin >> weight;

    for (int i = 1; i <= weight/2; i++) {
        if (i % 2 == 0 && (weight - i) % 2 == 0){
            cout << "YES";
            return 0;
        }
    }
    cout << "NO";
}
