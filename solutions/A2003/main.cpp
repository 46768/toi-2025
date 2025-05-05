#include <iostream>

void solve() {
	int n,b=0;
	int t[1002];
	std::cin>>n;
	t[0]=-1;t[n+1]=-1;
	for(int i=0;i<n;i++){
		std::cin>>t[i+1];
	}
	for(int i=1;i<n+1;i++){
		if(t[i-1]<=t[i]&&t[i]>=t[i+1]){
			b++;
		}
	}
	std::cout<<b<<std::endl;
}

int main() {
	solve();
}
