#include <iostream>
using namespace std;

int main() {
    
    for (int i = 1; i <= 19; i++) {
        for (int j = 1; j <= 19; j++) {
            if (j == 19) {
                cout << i << " * " << j << " = " << i * j << endl;
            }
            else if (j % 2 == 1) {
                cout << i << " * " << j << " = " << i * j << " / ";
            }
            if (j % 2 == 0) {
                cout << i << " * " << j << " = " << i * j << endl;
            }
        }
    }
    return 0;
}