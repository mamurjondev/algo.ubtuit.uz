#include <bits/stdc++.h>
using namespace std;
int main() {
 long n;
 cin>>n;
 long maxx = INT_MIN;  // !
long a[n+1]; // !
 for (int i=1; i<=n; i++){
    cin>>a[i];
    maxx = max(maxx, a[i]); // !
 }

 for (int i=1; i<=n; i++){
    if (maxx == a[i]){
      cout<<i;
    break;
        }

 }
 }    
