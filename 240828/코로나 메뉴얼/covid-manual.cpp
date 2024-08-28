#include <iostream>
using namespace std;

int main() {
    
    char a_sta, b_sta, c_sta;
    int a_temp, b_temp, c_temp;
    int cnt;
    cnt = 0;

    cin >> a_sta >> a_temp;
    cin >> b_sta >> b_temp;
    cin >> c_sta >> c_temp;

    if (a_sta == 'Y') {
        if (a_temp >= 37)
            cnt += 1;
    }

    if (b_sta == 'Y') {
        if (b_temp >= 37)
            cnt += 1;
    }

    if (c_sta == 'Y') {
        if (c_temp >= 37)
            cnt += 1;
    }

    if (cnt >= 2)
        cout << "E";
    else
        cout << "N";

    return 0;
}