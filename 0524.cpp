#include <bits/stdc++.h>

using namespace std;

int main()
{   double    l;
    cin>>l;
    double h=6.64e-34;
    double e=1.6e-19;
    double c=3e8;
    printf("%.4lf",(h*c*1e10/(l*e)));
    return 0;
}    
