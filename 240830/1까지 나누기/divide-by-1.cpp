#include <iostream>
using namespace std;

int main() {
    
    int n;
    cin >> n;
    
    int i = 1;
    while (i <= 5000) {
        n /= i;

        if (n <= 1) {
            cout << i;
            break;

        }

        i++;
    }
    return 0;
}