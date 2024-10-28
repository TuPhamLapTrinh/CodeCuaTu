#include <bits/stdc++.h>
using namespace std;
int n,a[1000001],tong=0;
int main()
{
    cin>>n;
    for(int i=1;i<=n;i++) cin>>a[i];
    for(int i=1;i<=n;i++)
    {
        if(a[i]%2==0)
        {
            tong+=a[i];
        }
    }
    cout<<tong;
    return 0;
}
