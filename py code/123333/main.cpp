#include <bits/stdc++.h>
using namespace std;
long long  abc[10000000], c ,a=0 , b=1 , n ;
bool kt(long long x )
{   if(x==1 ||x==0) return true ;
    while(x>0)
    {
        c=a+b ;
        a=b;
        b=c;
        if(c==x) return true ;
        else return false ;
    }
}
int main()
{
    cin>> n ;
    for( long long  j =1 ; j <= n ; j ++)
    {
        cin>> abc[j] ;
    }
    for(long long j = 1;j <= n ; j++)
    {
        if(kt(abc[j])== true) cout<< "IsFibo"<<endl ;
         else cout<< "IsNotFibo"<<endl ;
    }
        return 0 ;
}
