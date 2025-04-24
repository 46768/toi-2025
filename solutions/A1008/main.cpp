#include <iostream>
#include <string>
#include <cstring>

void solve() {
	std::string id;
	std::cin>>id;
	if(id.length()==13){
		std::cout<<"yes\n";
		return;
	}
	std::cout<<"no\n";
}

int main() {
	solve();
}
