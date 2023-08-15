#include <bits/stdc++.h>
using namespace std;

int main() {
    map<string, int> polygons = {{"Tetrahedron", 4}, {"Cube", 6}, {"Octahedron", 8}, 
                                    {"Dodecahedron", 12}, {"Icosahedron", 20}};

    int t;
    cin >> t;

    string shape;
    int total_faces = 0;
    for (int i = 0; i < t; i++) {
        cin >> shape;
        total_faces += polygons.at(shape);
    }

    cout << total_faces;
}