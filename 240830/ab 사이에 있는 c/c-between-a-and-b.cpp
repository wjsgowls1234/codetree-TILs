#include <iostream>
using namespace std;

int main() {
    
    int a, b, c;
    cin >> a >> b >> c;

    bool satisfeid = false;
    for (int i = a; i <= b; i++) {
        if (i % c == 0) {
            satisfeid = true;
        }
    }
    if (satisfeid == true) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
    return 0;
}