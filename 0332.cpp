#include<iostream>
 #include<math.h>
 #include<stdio.h>
 using namespace std;
 int main()  {
     double x,y;
     cin>>x>>y;
     double A=(x*x+1)/(x*x+(x+y*y)/(y*y+(y+x)/(fabs(x)+7)));
     double f=A+(cos(x)+1/cos(fabs(x)))/(1+sin(x)+1/sin(fabs(x)));
     printf("%.2f",f);


 }    
