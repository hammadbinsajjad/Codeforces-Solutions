#include <iostream>
using namespace std;

int main() {
    int n , k; cin >> n >> k; k -= 1;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int c  =0;
    int i = n - 1;
    while (i >= 0) {
        if (arr[i] != arr[k]) {
            c = i +1;
            break;
        }
        i -= 1;
    }
    if(c > k + 1) {
        cout << - 1 << endl; 
        return 0;
    }

    for (int i = k; i < n; i++) {
        if (arr[i] != arr[k]) {cout << - 1 << endl; return 0;}
    }
    cout << c << endl;
    return 0;
}