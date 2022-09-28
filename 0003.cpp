#include<iostream>
#include<iomanip>
using namespace std;
int main()
{
        float s, h, a;
        cin >> s >> h;
        a = 2*s / h;
        cout << setprecision(2) << fixed << a << endl;
}    
