#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int x, y, z;
    cin >> x >> y >> z;

    int a, b, c;

    b = sqrt((y * x) / z);
    a = x / b;
    c = y / b;
    cout << a*4 + b*4 + c*4 << endl;
}
