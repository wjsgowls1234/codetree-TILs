#include <iostream>
using namespace std;

int main() {
    
    int a;
    cin >> a;

    string rate = a == 100 ? "pass" : "failure";
    
    cout << rate;

    return 0;
}