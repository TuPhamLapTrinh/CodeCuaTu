#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n,d=0;
    cin>>n;
    while(n!=0)
    {
        n=n/10;
        d++;
    }
    cout<<d;


    return 0;
}
