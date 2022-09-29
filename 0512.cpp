#include <bits/stdc++.h>
using namespace std;
int main()
{
double J, m, d, T;
cin>>J>>m>>d;
float const gi=9.81;
T=2*M_PI*sqrt(1.0*J/(m*gi*d));
cout<<setprecision(4)<<fixed<<T;

   return 0;
}    
