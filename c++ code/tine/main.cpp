#include <iostream>
#include <ctime>
using namespace std;

class clock_console{
private:
	int hour, minute, second, milisecond, day, month, year;

	void run_time(){
		milisecond++;
		if (milisecond == 60){
			milisecond = 0;
			cout << "\a";
			second++;
			if (second >= 60){
				second = 0;
				minute++;
				if (minute == 60){
					minute = 0;
					hour++;
					if (hour == 24){
						hour = 0;
						day++;
						if (day == 1 + day_month(month)){
							day = 1;
							month++;
							if (month == 13){
								month = 1;
								year++;
								if (year == 2081){   // clock only run to 2080
									cout << "Out of battery" << endl;
									system("pause");
									exit(0);
								}
							}
						}
					}
				}
			}
		}
	}

	void clock_24h(){
		system("cls");
		cout << "       ,--.-----.--." << endl;
		cout << "       |--|-----|--|" << endl;
		cout << "       |--|     |--|" << endl;
		cout << "       |  |-----|  |" << endl;
		cout << "     __|--|     |--|__" << endl;
		cout << "    /  |  |-----|  |  \\ " << endl;
		cout << "   /    \\_|-----|_/    \\ " << endl;
		cout << "  /   ______---______   \\/\\ " << endl;
		cout << " /   /               \\   \\/" << endl;
		cout << "{   /      Armani     \\   }" << endl;
		cout << "|  {                   }  |-," << endl;

		cout << (hour < 10 ? "|  |    0" : "|  |    ") << hour << (minute < 10 ? " : 0" : " : ") << minute
			<< (second < 10 ? " : 0" : " : ") << second << "   |  | |" << "\t\t    anh2uantran@gmail.com" << endl;

		/*
		if (hour < 10)  cout << "|  |    0" << hour;
		else  cout << "|  |    " << hour;

		if (minute < 10)  cout << " : 0" << minute;
		else cout << " : " << minute;

		if (second < 10)  cout << " : 0" << second << "   |  | |" << endl;
		else cout << " : " << second << "   |  | |" << endl;
		*/
	}

	void clock_12h(){
		system("cls");
		cout << "       ,--.-----.--." << endl;
		cout << "       |--|-----|--|" << endl;
		cout << "       |--|     |--|" << endl;
		cout << "       |  |-----|  |" << endl;
		cout << "     __|--|     |--|__" << endl;
		cout << "    /  |  |-----|  |  \\ " << endl;
		cout << "   /    \\_|-----|_/    \\ " << endl;
		cout << "  /   ______---______   \\/\\ " << endl;
		cout << " /   /               \\   \\/" << endl;
		cout << "{   /      Armani     \\   }" << endl;
		cout << "|  {                   }  |-," << endl;

		if (hour == 0)       cout << "|  |  " << hour + 12;
		else if (hour < 10)  cout << "|  |  0" << hour;
		else if (hour <= 12) cout << "|  |  " << hour;
		else if (hour > 12 && hour < 22)  cout << "|  |  0" << hour - 12;
		else cout << "|  |  " << hour - 12;

		if (minute < 10)  cout << " : 0" << minute;
		else cout << " : " << minute;

		if (second < 10)  cout << " : 0" << second;
		else cout << " : " << second;

		if (hour < 12) cout << "  AM" << " |  | |" << "\t\t    anh2uantran@gmail.com" << endl;
		else cout << "  PM" << " |  | |" << "\t\t    anh2uantran@gmail.com" << endl;
	}

	void calender_number(){
		cout << (day < 10 ? "|  {     0" : "|  {     ") << day << "/"
			<< (month < 10 ? "0" : "") << month << "/" << year << "    }  |-'" << endl;
		cout << "{   \\                 /   }" << endl;
		cout << " \\   `------___------'   /\\ " << endl;
		cout << "  \\     __|-----|__     /\\/" << endl;
		cout << "   \\   /  |-----|  \\   /" << endl;
		cout << "    \\  |--|     |--|  /" << endl;
		cout << "     --|--|     |--|--" << endl;
		cout << "       |  |-----|  |" << endl;
		cout << "       |--|     |--|" << endl;
		cout << "       |--|-----|--|" << endl;
		cout << "       `--'-----`--'" << endl;
		cout << endl;
	}

	void calender_name(){
		cout << "|  {";
		switch (month){
		case 1: cout << "  January "
			<< (day < 10 ? "0" : "") << day << ", " << year << " }  |-'" << endl;
			break;
		case 2: cout << " February "
			<< (day < 10 ? "0" : "") << day << ", " << year << " }  |-'" << endl;
			break;
		case 3: cout << "   March "
			<< (day < 10 ? "0" : "") << day << ", " << year << "  }  |-'" << endl;
			break;
		case 4: cout << "   April "
			<< (day < 10 ? "0" : "") << day << ", " << year << "  }  |-'" << endl;
			break;
		case 5: cout << "    May "
			<< (day < 10 ? "0" : "") << day << ", " << year << "   }  |-'" << endl;
			break;
		case 6: cout << "   June "
			<< (day < 10 ? "0" : "") << day << ", " << year << "   }  |-'" << endl;
			break;
		case 7: cout << "   July "
			<< (day < 10 ? "0" : "") << day << ", " << year << "   }  |-'" << endl;
			break;
		case 8: cout << "  August "
			<< (day < 10 ? "0" : "") << day << ", " << year << "  }  |-'" << endl;
			break;
		case 9: cout << " September "
			<< (day < 10 ? "0" : "") << day << ", " << year << "}  |-'" << endl;
			break;
		case 10: cout << "  October "
			<< (day < 10 ? "0" : "") << day << ", " << year << " }  |-'" << endl;
			break;
		case 11: cout << " November "
			<< (day < 10 ? "0" : "") << day << ", " << year << " }  |-'" << endl;
			break;
		case 12: cout << " December "
			<< (day < 10 ? "0" : "") << day << ", " << year << " }  |-'" << endl;
			break;
		}
		cout << "{   \\                 /   }" << endl;
		cout << " \\   `------___------'   /\\ " << endl;
		cout << "  \\     __|-----|__     /\\/" << endl;
		cout << "   \\   /  |-----|  \\   /" << endl;
		cout << "    \\  |--|     |--|  /" << endl;
		cout << "     --|--|     |--|--" << endl;
		cout << "       |  |-----|  |" << endl;
		cout << "       |--|     |--|" << endl;
		cout << "       |--|-----|--|" << endl;
		cout << "       `--'-----`--'" << endl;
		cout << endl;
	}

	int day_month(int month){
		switch (month){
		case 1:
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12: return 31;
			break;
		case 6:
		case 4:
		case 9:
		case 11: return 30;
			break;
		case 2: return 28;
			break;
		}
	}

public:
	clock_console(){
		time_t full_time;
		time(&full_time);
		struct tm *sub_time;
		sub_time = localtime(&full_time);
		this->milisecond = 0;
		this->second = sub_time->tm_sec;
		this->minute = sub_time->tm_min;
		this->hour = sub_time->tm_hour;
		this->day = sub_time->tm_mday;
		this->month = 1 + sub_time->tm_mon;
		this->year = 1900 + sub_time->tm_year; // tm_year = nam hien tai  - 1900
		/*
		note:
		struct tm {
		int tm_sec;  //  0 - 61
		int tm_min;  //  0 - 59
		int tm_hour; //  0 - 23
		int tm_mday; //  1 - 31
		int tm_mon;  //  0 - 11
		int tm_year; // bat dau tu 1900
		};
		*/
	}

	void run(){
		int option1, option2;
		do{
			system("cls");
			cout << "1 - 12h" << endl;
			cout << "2 - 24h" << endl;
			cin >> option1;
		} while (option1 < 1 || option1 > 2);

		do{
			system("cls");
			cout << "1 - DD/MM/YYY" << endl;
			cout << "2 - Month Day, Year" << endl;
			cin >> option2;
		} while (option2 < 1 || option2 > 2);

		if (option1 == 1 && option2 == 1){
			do{
				run_time();
				clock_12h();
				calender_number();
			} while (1);
		}
		else if (option1 == 1 && option2 == 2){
			do{
				run_time();
				clock_12h();
				calender_name();
			} while (1);
		}
		else if (option1 == 2 && option2 == 1){
			do{
				run_time();
				clock_24h();
				calender_number();
			} while (1);
		}
		else{
			do{
				run_time();
				clock_24h();
				calender_name();
			} while (1);
		}
	}

	void new_time(){
		char temp;
		do{
			system("cls");
			cout << "Input Second : Minute : Hour" << endl;
			cin >> second >> temp >> minute >> temp >> hour;
			cout << "Input YYYY/MM/DD" << endl;
			cin >> year >> temp >> month >> temp >> day;
		} while (second<0 || second>59 || minute<0 || minute>59 || hour<0 || hour>23
			|| year<1994 || year>2080 || month<1 || month>12 || day<1 || day>day_month(month));
		run();
	}
};

int main(){
	clock_console now;

	int option;
	do{
		system("cls");
		cout << "       | |              | |                                       | |       " << endl;
		cout << "  ____ | |  ___    ____ | |  _     ____  ___   ____    ___   ___  | |  ____ " << endl;
		cout << " / ___)| | / _ \\  / ___)| | / )   / ___)/ _ \\ |  _ \\  /___) / _ \\ | | / _  )" << endl;
		cout << "( (___ | || |_| |( (___ | |< (   ( (___| |_| || | | ||___ || |_| || |( (/ / " << endl;
		cout << " \\____)|_| \\___/  \\____)|_| \\_)   \\____)\\___/ |_| |_|(___/  \\___/ |_| \\____)" << endl;
		cout << endl;
		cout << "1 - Run" << endl;
		cout << "2 - Set new time" << endl;
		cout << "3 - Exit" << endl;
		cin >> option;
	} while (option < 1 || option > 3);

	switch (option){
	case 1: now.run();
		break;
	case 2: now.new_time();
		break;
	case 3: return 0;
		break;
	}
	system("pause");
	return 0;
}
