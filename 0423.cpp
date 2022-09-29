#include <bits/stdc++.h>
using namespace std;
int main()
{
ios::sync_with_stdio(false);
    cin.tie(0);
long long int n,a[200000],s=-11111111110,m,x=0,r=-11111,b,y=0;
cin>>n;
for (int i=0;i<n;i++)
{
        
        
            cin>>a[i];
            if (a[i]>s)
{
s=a[i];
y=i;
}
        


}
for (int i=0;i<n;i++)
{
b=a[i];
a[i]=s;
a[y]=b;
s=-100000000000;
for (int j=i+1;j<n;j++)
{
if (a[j]>s)
{
s=a[j];
y=j;
}
}
}
if (a[n-1]*a[n-2]*a[0]>a[0]*a[1]*a[2])
{
cout<<a[n-1]*a[n-2]*a[0];
}else
{
cout<<a[0]*a[1]*a[2];
}

return 0;
}    
