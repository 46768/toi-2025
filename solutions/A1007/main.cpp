#include <iostream>

const char v[5]={'a','e','i','o','u'};

void solve() {
	char c;
	std::cin>>c;
	for(int i=0;i<5;i++){
		if(c==v[i]){
			std::printf("yes\n");
			return;
		}
	}
	std::printf("no\n");
}

int main() {
	solve();
}
