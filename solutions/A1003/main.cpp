#include <iostream>

void solve() {
	int largest = -99999;
	for (int i = 0; i < 3; i++) {
		int num;
		std::cin >> num;
		if (num > largest) largest = num;
	}
	std::printf("%d\n", largest);
}

int main() {
	solve();
}
