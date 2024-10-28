#include <bits/stdc++.h>

using namespace std;
int n;
float s=0;
int main()
{
    cin>>n;
    for(int i=1;i<=n;i++) s = s + 1.0 / i;
    cout<<s;

    return 0;
}
