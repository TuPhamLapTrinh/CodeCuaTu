#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n,d=0;
    cin>>n;
    while(n!=0)
    {
        d++;
        n=n/10;
    }
    cout<<d;
        return 0;
}
