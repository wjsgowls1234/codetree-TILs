#include <iostream>
using namespace std;

int main() {
    
    int a, b, c;
    cin >> a >> b >> c;

    if ((a > b && b > c) && (a == c)) {
        cout << "1 ";
    }
    else {
        cout << "0 ";
    }

    cout << (a == b == c);
    return 0;
}