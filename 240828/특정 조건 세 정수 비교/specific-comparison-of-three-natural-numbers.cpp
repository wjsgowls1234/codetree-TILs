#include <iostream>
using namespace std;

int main() {
    
    int a, b, c, minimum;
    cin >> a >> b >> c;

    if (a > b && b > c) {
        minimum = c;
    }
    else if (a > c && c > b) {
        minimum = b;
    }
    else if (b > a && a > c) {
        minimum = c;
    }
    else if (b > c && c > a) {
        minimum = a;
    }
    else if (c > b && b > a) {
        minimum = a;
    }
    else if (c > a && a > b) {
        minimum = b;
    }

    if (a == minimum) {
        cout << "1 ";
    }
    else {
        cout << "0 ";
    }

    if (a == b == c) {
        cout << 1;
    }
    else {
        cout << 0;
    }
    return 0;
}