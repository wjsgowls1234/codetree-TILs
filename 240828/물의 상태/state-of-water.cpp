#include <iostream>
using namespace std;

int main() {
    
    int n;
    cin >> n;

    if (n < 10) {
        cout << "ice" << endl;
    }
    else if (n >= 100) {
        cout << "vapor" << endl;
    }
    else {
        cout << "water" << endl;
    }

    return 0;
}