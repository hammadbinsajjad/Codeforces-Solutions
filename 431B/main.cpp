#include <bits/stdc++.h>
using namespace std;

#define MIN_INT -1

int f(int arr[5], int graph[][5]) {
    return (
        graph[arr[0]][arr[1]] + graph[arr[1]][arr[0]] + graph[arr[2]][arr[3]] + graph[arr[3]][arr[2]] + 
        graph[arr[1]][arr[2]] + graph[arr[2]][arr[1]] + graph[arr[3]][arr[4]] + graph[arr[4]][arr[3]] +
        graph[arr[2]][arr[3]] + graph[arr[3]][arr[2]] + 
        graph[arr[3]][arr[4]] + graph[arr[4]][arr[3]]
    );
}

int main() {
    int g[5][5];

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            cin >> g[i][j];
        }
    }

    int arr[5] = {0,1,2,3,4};
    int mf = MIN_INT;
    do {
        mf = max(mf, f(arr, g));
    }while(next_permutation(arr, arr + 5));

    cout << mf << endl;
}