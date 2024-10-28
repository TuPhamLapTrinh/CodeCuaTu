#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n,d=1;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        if(n%i==0) d = d * i;
    }
    cout<<d;
    return 0;
}
