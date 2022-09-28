#include <bits/stdc++.h>

using namespace std;

int main()
{   double    l;
    cin>>l;
    double h=6.64e-34;
    double k=1.38e-23;
    double c=3e8;
    printf("%.4lf",(2*h*c*1e6/(3*k*l)));
    return 0;
}    
