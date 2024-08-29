#include <iostream>
using namespace std;

int main() {
    
    int n;
    cin >> n;

    int cnt = 0, sum = 0;

    for (int i = 1; i <= n; i++) {
        int a;
        cin >> a;

        cnt++;
        sum += a;
    }

    cout << fixed;
    cout.precision(1);

    cout << sum << " " << (double)sum / cnt;
    return 0;
}