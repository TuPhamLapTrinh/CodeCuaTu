#include <bits/stdc++.h>
using namespace std;
bool SNT(int n)
{
    if(n<2) return false;
    for(int i=2;i<=sqrt(n);i++)
    {
        if(n%i==0) return false;
    }
    return true;
}
int main()
{
    int n;
    cin>>n;
   if(SNT(n)) cout<<"la so nguyen to";
   else cout<<"ko la SNT";


    return 0;
}
