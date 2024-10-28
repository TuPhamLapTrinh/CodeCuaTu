#include <bits/stdc++.h>
using namespace std;
int n,tong=0;
float a[102];
void nhap()
{
    cin>>n;
    for(int i=1;i<=n;i++) cin>>a[i];
}
void xuat()
{

    for(int i=1;i<=n;i++)
        tong+=a[i];
}
void kq()
{
    cout<<tong;
}
int main()
{
    nhap();
    xuat();
    kq();

    return 0;
}
