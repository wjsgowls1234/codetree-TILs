#include <iostream>
using namespace std;

int main() {
    
    int cnt = 0;

    for (int i = 1; i <= 5; i++) {
        if (i % 2 == 0) {
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}