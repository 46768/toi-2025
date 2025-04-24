#include <iostream>

void solve() {
	int a;
	char s;
	std::cin>>a;
	std::cin>>s;
	if(a<18||(s=='s'||s=='S')){
		std::cout<<"20\n";
		return;
	}
	std::cout<<"50\n";
}

int main() {
	solve();
}
