#include <iostream>
using namespace std;

int main() {
    
    int a = 3, b = 8;
    int prod = 1;

    for (int i = a; i <= b; i++) {
        if (i % 2 == 0) {
            prod *= i;
        }
    }

    cout << prod;
    return 0;
}