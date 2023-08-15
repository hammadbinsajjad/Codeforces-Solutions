#include <iostream>
#include <iomanip>

int main() {
    long long h, l;
    std::cin >> h >> l;

    

    std::cout << std::setprecision(16) << std::fixed << (l*l - h*h) /(long double) (2*h) << std::endl;
}