#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n,maxn=1;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        if(n%i==0)
        {
            if(i%2!=0)
            {
                if(i > maxn)
                {
                    maxn=i;
                }
               // cout<<i;
            }
        }
    }
    cout<<maxn;
    return 0;
}
