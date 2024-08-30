#include <iostream>
using namespace std;

int main() {
    
    int n;
    cin >> n;
    bool satisfied = false;

    for (int i = 2; i <= n; i++) {
        int cnt = 0;

        if (n % i == 0) {
            cnt++;
        }

        if (cnt == 1) {
            satisfied = true;
        }
    }

    if (satisfied == true) {
        cout << 'P';
    }
    else {
        cout << 'C';
    }
    return 0;
}