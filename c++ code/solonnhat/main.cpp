#include <bits/stdc++.h>
using namespace std;
int a,b,c,maxn;
void Nhapxuat()
{
    cout<<"Nhap vao a = ";
    cin>>a;
    cout<<"Nhap vao b = ";
    cin>>b;
    cout<<"Nhap vao c = ";
    cin>>c;
}
void So_lon_Nhat()
{
    maxn = a;
    if(maxn < b) maxn=b;
    if(maxn < c) maxn=c;

}
void Ketqua()
{
    cout<<"So lon nhat trong ba so "<<a<<","<<b<<","<<c<<" la: "<<maxn;
}
int main()
{
    Nhapxuat();
    So_lon_Nhat();
    Ketqua();

    return 0;
}
