#include <cstdlib>
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
    int n, a[50],min=a[0], s=0;
    cin>>n;
    for(int i=0; i<n; i++) {
    cin>>a[i];
    if(min>a[i]) min=a[i];
    }
    
    for(int i=0; i<n; i++){ 
    if(a[i]==min)
    s++;
}
cout<<s;

}    
