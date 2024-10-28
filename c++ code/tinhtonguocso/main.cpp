#include <bits/stdc++.h>
using namespace std;
int n,d=0;
int main()
{
    cout<<"Nhap n: ";cin>>n;
    for(int i=1;i<=n;i++)
    {
        if(n % i == 0)
        {
            d=d+i;
        }
    }
    cout<<"Ket qua la:"<<d;

    return 0;
}
