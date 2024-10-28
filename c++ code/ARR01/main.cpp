#include <bits/stdc++.h>
using namespace std;
int n,a[52];
void Nhap()
{
    cout<<"Nhap vao n= "; cin>>n;
    for(int i=1;i<=n;i++)
    {
       cout << "Nhap vao phan tu a[" << i << "] : ";
       cin>>a[i];
    }
}
void xuat()
{
    for(int i=1;i<=n;i++)
        cout<<a[i]<<" ";
}
int main()
{
    Nhap();
    cout<<"Mang sau khi nhap tu ban phim la: ";
    xuat();
    return 0;
}
