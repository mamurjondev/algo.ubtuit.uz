#include <iostream>
 #include <iomanip>

 using namespace std;

 int main()
 { double x, a, y, b, A, B;
   cin>>x>>a>>y>>b;
   A=a/x; B=b/y;
   cout<<setprecision(2)<<fixed<<A<<" "<<B;

     return 0;
 }    
