#include <iostream>
 #include <iomanip>
 #include <cmath>

 using namespace std;

 int main()
 { double r, h, v;
 cin>>r>>h;
   v=r*r*h*M_PI;
   cout<<setprecision(2)<<fixed<<v;
     return 0;
 }    
