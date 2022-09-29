#include<bits/stdc++.h>
using namespace std;
int k;
main ()
{
string s;
getline(cin,s);
char m[10] = {'a','i','o','e','u','A','I','O','E','U'};
for(int i=0; i<s.size();i++)
   for(int j=0; j<10; j++)
       if(s[i]==m[j]) k++;
   cout << k;    
}    
