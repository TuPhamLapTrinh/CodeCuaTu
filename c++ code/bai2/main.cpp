#include <bits/stdc++.h>
using namespace std;
int n;
bool SNT(int x)
{
    if (x < 2) return false;
    for(int i=2;i<sqrt(x);i++)
        if(x % i == 0) return false;
        return true;
}
int tach_so(int a)
{

    int t=0;
    while(a!=0)
    {
        int c = a % 10;
        a = a / 10;
        t=t+c;
    }
    return t;
}
int main()
{
   // cout << "Hello world!" << endl;
   freopen("BAI2.INP","r",stdin);
   freopen("BAI2.OUT","w",stdout);
   cin>>n;
   if(SNT(tach_so(n)))
     cout<<"OK";
   else
     cout<<"NO OK";
   return 0;
}
