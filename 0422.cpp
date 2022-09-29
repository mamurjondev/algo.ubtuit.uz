#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,i;
    cin>>n;
    int a[n],b;
    for(i=1; i<=n; i++){
        cin>>a[i];
    }
    for(i=1; i<=n; i++){
      if(i%2==1){
          if(a[i]%2==0){
                b=a[1];
            if(a[i]>b)
                b=a[i];
          }
      }
    }
    cout<<b;
}    
