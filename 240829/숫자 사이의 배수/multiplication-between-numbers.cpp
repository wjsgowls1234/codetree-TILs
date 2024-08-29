#include <iostream>
using namespace std;

int main() {
    
    int a, b;
    cin >> a >> b;
    int cnt = 0, sum = 0;

    for (int i = a; i <= b; i++) {
        if (i % 5 == 0 || i % 7 == 0) {
            cnt++;
            sum += i;
        }
    }

    cout << fixed;
    cout.precision(1);

    cout << sum << " " << (double)sum / cnt;
    return 0;
}