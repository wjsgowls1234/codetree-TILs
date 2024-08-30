#include <iostream>
using namespace std;

int main() {
    
    int n;
    cin >> n;

    int cnt = 0, x = 1;

    while (x != n) {
        x *= 2;
        cnt++;
    }

    cout << cnt;
    return 0;
}