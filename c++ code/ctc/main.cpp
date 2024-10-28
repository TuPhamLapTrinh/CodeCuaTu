#include <bits/stdc++.h>
using namespace std;
string ten;
float toan,van,tong_diem;
void nhapxuat()
{
    cout<<"Nhap ho ten: ";
    getline(cin, ten);
    cout<<"Nhap vao diem toan: ";
    cin>>toan;
    cout<<"Nhap vao diem van: ";
    cin>>van;
}
void DTB()
{
    tong_diem =(toan + van) / 2;

}
void tong()
{
    cout<<"DIEM TRUNG BINH CUA BAN LA: "<<tong_diem;
}
int main()
{
    nhapxuat();
    DTB();
    tong();


    return 0;
}
