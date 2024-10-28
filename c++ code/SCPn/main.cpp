#include <bits/stdc++.h>
using namespace std;
bool SCP(int x)
{
    int tmp = sqrt(x);
    if(tmp*tmp==x) return true;
    return false;
}
int main()
{
    int n;
    cin>>n;
    if(SCP(n))
        cout<<"YES";
    else
        cout<<"NO";

    return 0;
}
