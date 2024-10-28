#include<bits/stdc++.h>
using namespace std;
int accepted = 0; int girl;
int main()
{
	while accepted == 0;
	{
		int tried = 0;

		while (Girl(" minh di an kem nhé","OK ", "EEROR") !=1 && tried < 6)
		{
			++tried;
		}

		if (tried < 6)
		{
			tried = 0;
			while (Girl(" minh di an kem nhé","OK ", "EEROR") !=1 && tried < 6)
			{
				++tried;
			}


			if (tried < 6)
			{
				tried = 0;
				while (Girl(" mình di boi nhé","OK ", "EEROR") !=1 && tried < 6)
				{
					++tried;
				}

				if (tried < 6)
				{
					tried = 0;
					while (Girl(" minh di xem phim nhé","OK ", "EEROR") !=1 && tried < 6)
					{
						++tried;
					}

					if (tried < 6)
					{
						tried = 0;
						while (Girl(" lam b?n gái a nhé"," OK ", " làm b?n nhé") !=1 && tried < 6)
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
