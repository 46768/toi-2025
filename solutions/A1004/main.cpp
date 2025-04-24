#include <iostream>

const int pass[3] = {5, 20, 25};

void solve() {
	int is_fail = 0;
	for (int i = 0; i < 3; i++) {
		int num;
		std::cin >> num;
		is_fail |= num < pass[i];
	}
	if (is_fail) {
		std::printf("fail\n");
	} else {
		std::printf("pass\n");
	}
}

int main() {
	solve();
}
