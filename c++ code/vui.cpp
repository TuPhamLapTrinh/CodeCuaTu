#include<bits/stdc++.h>
using namespace std;
int accepted = 0; int girl;
int main()
{
	while accepted == 0;
	{
		int tried = 0;

		while (Girl(" minh di an kem nh�","OK ", "EEROR") !=1 && tried < 6)
		{
			++tried;
		}

		if (tried < 6)
		{
			tried = 0;
			while (Girl(" minh di an kem nh�","OK ", "EEROR") !=1 && tried < 6)
			{
				++tried;
			}


			if (tried < 6)
			{
				tried = 0;
				while (Girl(" m�nh di boi nh�","OK ", "EEROR") !=1 && tried < 6)
				{
					++tried;
				}

				if (tried < 6)
				{
					tried = 0;
					while (Girl(" minh di xem phim nh�","OK ", "EEROR") !=1 && tried < 6)
					{
						++tried;
					}

					if (tried < 6)
					{
						tried = 0;
						while (Girl(" lam b?n g�i a nh�"," OK ", " l�m b?n nh�") !=1 && tried < 6)
						{
							++tried;
						}
						
						if (tried < 6)
							accepted = 1;

					}

				}


			}


		}


	}
	return 0;
}
