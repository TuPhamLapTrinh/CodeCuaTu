#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n,s=0;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        if(n%i==0)
            s=s+i;
    }
    if(s==n)
        cout<<"So hoan hao";
    else
        cout<<"So ko hoan hao";
    return 0;
}
