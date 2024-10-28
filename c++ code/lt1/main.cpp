#include <bits/stdc++.h>
using namespace std;
bool SNT(int x)
{
    if (x < 2) return false;
    for(int i=2;i<=sqrt(x);i++)
        if (x % i == 0) return false;
    return true;
}
int main()
{
    freopen("B1.INP","r",stdin);
    freopen("B1.OUT","w",stdout);
    int n;
    cin>>n;
    if (SNT(n)) cout<<"YES";
    else cout<<"NO";


    return 0;
}
