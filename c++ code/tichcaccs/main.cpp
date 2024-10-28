#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n,d=1;
    cin>>n;
    while(n!=0)
    {
        d=d*(n%10);
        n=n/10;
    }
    cout<<d;
    return 0;
}
