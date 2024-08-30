#include <iostream>
using namespace std;

int main() {
    
    int sum = 0;
    int cnt = 0;

    while (1) {
        int age;
        cin >> age;
        
        double avg;
        avg = (double)sum / cnt;

        if (age <= 19 || age >= 30) {
            cout << fixed;
            cout.precision(2);
            cout << avg;

            break;
        }

        cnt++;
        sum += age;

    }
    return 0;
}