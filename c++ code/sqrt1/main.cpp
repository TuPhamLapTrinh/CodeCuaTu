#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    float d=0;
    cin>>n;
    d=sqrt((float)2);
    for(int i=2;i<=n;i++)
    {
        d=sqrt(i+d);
    }
    cout<<d;
    return 0;
}
