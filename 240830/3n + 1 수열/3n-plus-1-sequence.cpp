#include <iostream>
using namespace std;

int main() {
    
    int n;
    cin >> n;
    int cnt = 0;

    while (true) {

        if (n == 1) {
            break;
        }

        if (n % 2 == 0) {
            n /= 2;
        }
        else {
            n = n * 3 + 1;
        }

        cnt++;

    }

    cout << cnt;
    return 0;
}