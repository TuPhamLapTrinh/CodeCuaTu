#include <bits/stdc++.h>
using namespace std;
int main()

{

    int n,d=0,i;

    cin>>n;

    while(i<=n)

    {

        if (n%i==0) d=d+i;

        i++;
    }

        cout<<d;

    return 0;

}
