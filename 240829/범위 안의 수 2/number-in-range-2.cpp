#include <iostream>
using namespace std;

int main() {
    
    int cnt = 0, sum = 0;

    for (int i = 1; i <= 10; i++) {

        int n;
        cin >> n;

        if (n >= 0 && n <= 200) {
            cnt++;
            sum += n;
        }
    }
    
    cout << fixed;
    cout.precision(1);

    cout << sum << " " << (double)sum / cnt;
    return 0;
}