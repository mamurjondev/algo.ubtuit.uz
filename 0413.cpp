#include<bits/stdc++.h>
 using namespace std; 
 int main () 
 {
     int array[1000]; 
     int n; cin>>n; 
     for (int i=0; i<n; i++)
     cin>>array[i];
     sort(array, array+n); 
     for (int i=0; i<n; i++)
     cout<<array[i]<<" "; 
     cout<<endl; 
     for (int i=n-1; i>=0; i--)
     cout<<array[i]<<" "; 
 }
