#include <iostream>

const char* season[4] = {"winter", "spring", "summer", "fall"};

void solve() {
	int month, day;
	int si = 0;
	std::cin >> month;
	std::cin >> day;

	if (month <= 3) {
		si = 0;
	} else if(month<=6){
		si = 1;
	}else if(month<=9){
		si=2;
	}else{
		si=3;
	}
	if(day>=21 && !(month%3)){
		si++;
	}
	si = si % 4;
	std::cout << season[si] << std::endl;
}

int main() {
	solve();
}
