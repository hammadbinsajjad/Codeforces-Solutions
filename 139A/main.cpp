#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[7];
    for (int i = 0; i < 7; i++) {
        cin >> arr[i];
    }

    int i = 0;
    while(n > 0) {
        n -= arr[i];
        i = (i + 1) % 7;
    }
    i = i - 1;
    if (i < 0) i = 7 + i + 1;
    else i = i + 1;
    cout << i << endl;
}
