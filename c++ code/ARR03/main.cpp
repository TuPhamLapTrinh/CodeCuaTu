#include <bits/stdc++.h>
using namespace std;
int n,maxn=-1e9;
float a[1000001];
int main()
{
    cin>>n;
    for(int i=1;i<=n;i++) cin>>a[i];
    for(int i=1;i<=n;i++)
    {
        if(maxn < a[i])
        {
            maxn=i;
        }
    }
    cout<<maxn;
     return 0;
}
