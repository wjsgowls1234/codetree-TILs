#include <iostream>
using namespace std;

int main() {
    
    int n;
    cin >> n;

    if (n < 0) {
        cout << "ice" << endl;
    }
    else if (n >= 100) {
        cout << "vapor" << endl;
    }
    else {
        cout << "water";
    }

    return 0;
}