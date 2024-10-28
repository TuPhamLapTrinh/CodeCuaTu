#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin >> n;
	int i = 1;
	int demuoc = 0;
	while (i <= n)
        {
            if (n % i == 0)
            {
                demuoc++;
            }
            i++;
	    }
	cout << demuoc;
	return 0;
}
