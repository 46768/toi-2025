#include <iostream>
#include <string>

void solve() {
	std::string first_name;
	std::string last_name;
	char initials[5];

	std::getline(std::cin, first_name);
	std::getline(std::cin, last_name);

	initials[0] = first_name[0];
	initials[1] = first_name[1];
	initials[2] = last_name[0];
	initials[3] = last_name[1];
	initials[4] = 0;

	std::cout << "Hello " << first_name << " " << last_name << std::endl;
	std::cout << initials << std::endl;
}

int main() {
	solve();
}
