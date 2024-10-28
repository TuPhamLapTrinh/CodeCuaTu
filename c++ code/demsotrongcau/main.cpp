#include <bits/stdc++.h>
using namespace std;
string s;
int d=0;
int main()
{
    getline(cin , s);
    for(int i=0;i<s.size();i++)
        {
            if(s[i]>='0'&&s[i]<='9')
                d++;
        }
        cout<<d;
    return 0;
}
