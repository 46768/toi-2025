#include <iostream>

void solve() {
	int num, div;
	std::cin>>num;
	std::cin>>div;
	if (!(num%div)){
		std::printf("yes\n");
	}else{
		std::printf("no\n");
	}
}

int main() {
	solve();
}
