#include<bits/stdc++.h>
#include<windows.h>
using namespace std;

int main()
{
	HANDLE h= GetStdHandle(STD_OUTPUT_HANDLE);
    ifstream file;
    file.open("F:tu.txt",ios_base::in);
    string line;
    while (!file.eof())
    {
        getline(file, line);
        SetConsoleTextAttribute(h,6);
        cout<< line << "\n";
        Sleep(50);

    }
    system("pause");
}
 	
