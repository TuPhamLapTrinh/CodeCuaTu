#include<bits/stdc++.h>
using namespace std;
int main() {
    string s,s1;
    getline(cin,s);
    getline(cin,s1);
    int check=s.find(s1);
    if (check>-1) {
        cout<<"YES";
    } else {
        cout<<"NO";
    }
    return 0;
}
