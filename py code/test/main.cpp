#include<iostream>
#include<unistd.h>

int main()
{
    std::string res = "";

    std::cout << std::endl << std::endl;
    for(auto x : res)
        {
        std::cout << x;
        usleep(35000);
    }

    std::cout << std::endl << std::endl;

    return 0;
}
