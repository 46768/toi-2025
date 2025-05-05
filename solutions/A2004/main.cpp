#include <iostream>

void solve() {
	int n,p[301]={0},s=0;
	std::cin>>n;
	for(int i=0;i<n;i++){
		std::cin>>p[0];
		p[p[0]]++;
	}
	for(int i=1;i<301;i++){
		s+=s>=p[i]?0:p[i]-s;
	}
	std::cout<<s<<std::endl;
}

int main() {
	solve();
}
