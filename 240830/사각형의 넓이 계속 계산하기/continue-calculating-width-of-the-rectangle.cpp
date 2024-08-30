#include <iostream>
using namespace std;

int main() {
    
    while(1) {

        int a, b;
        char c;

        cin >> a >> b >> c;

        int s = a * b;

        cout << s << endl;

        if (c == 'C') {
            break;
        }
    }
    return 0;
}