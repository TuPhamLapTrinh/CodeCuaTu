#include <bits/stdc++.h>
using namespace std;
int n,i=0;
float s=0;
int main()
{
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        if((s+i) < n)
        {
            s=s+i;
        }
    }
    cout<<i;

    return 0;
}
