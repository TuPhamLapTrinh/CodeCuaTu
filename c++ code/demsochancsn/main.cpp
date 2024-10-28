#include <iostream>

using namespace std;

int main()
{
    int n;
    cin>>n;
    int d=0;
    while (n!=0)
    {
        if(n%2==0)
        {
            d=d+n%10;
        }
        n=n/10;

    }
    cout<<d;
    return 0;
}
