#include <iostream>

void solve() {
	int s1,s2;
	std::cin>>s1;std::cin>>s2;
	std::printf("%d\n%s\n",s1+s2,(s1+s2)>=50?"pass":"fail");
}

int main() {
	solve();
}
