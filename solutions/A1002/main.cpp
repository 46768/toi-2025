#include <iostream>

const int coins[4] = {10, 5, 2, 1};

void solve() {
	int coins_taken[4] = {0, 0, 0, 0};
	int amount;
	std::cin >> amount;

	int i = 0;
	while (amount > 0) {
		if (amount >= coins[i]) {
			amount -= coins[i];
			coins_taken[i]++;
		} else {
			i++;
		}
	}

	for (int i = 0; i < 4; i++) {
		std::printf("%d = %d\n", coins[i], coins_taken[i]);
	}
}

int main() {
	solve();
}
