#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    float s=1,d;
    cin>>n;
    d=sqrt((float)0);
    for(int i=1;i<=n;i++)
    {
        s=s*i;
        sqrt(s+d);
    }
    cout<<s;
    return 0;
}
