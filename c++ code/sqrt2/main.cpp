#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    float d=0;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        d=sqrt(i+d);
    }
    cout<<d;
    return 0;
}
