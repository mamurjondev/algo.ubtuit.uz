#include <bits/stdc++.h>

using namespace std;

int main()
{
    string str,num_in_base;
    unsigned long long n,base,ost;
    cin>>n>>base;
    while(n>0)
    {
        ost=n%base;
        if(ost>9)
        {
            if(ost==10)
                num_in_base+='a';
            else if(ost==11)
                num_in_base+='b';
            else if(ost==12)
                num_in_base+='c';
            else if(ost==13)
                num_in_base+='d';
            else if(ost==14)
                num_in_base+='e';
            else if(ost==15)
                num_in_base+='f';
        }
        else
        {
            stringstream ss;
            ss<<ost;
            ss>>str;
            num_in_base+=str;
        }
        n/=base;
    }
    for(int i=num_in_base.length()-1;i>=0;i--)
        cout<<num_in_base[i];
}
