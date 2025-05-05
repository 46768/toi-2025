#include <iostream>
#include <deque>

void solve() {
	int n,g[900];
	char c;
	std::cin>>n;
	for(int i=0;i<n*n;i++){
		std::cin>>c;
		g[i]=c=='X'?0:1;
	}
	std::deque<int> q={(n*n)-1};
	int a=0,cu,x,y;
	while(!q.empty()){
		cu=q.front();
		y=cu/n;x=cu%n;
		q.pop_front();
		if(g[cu]){
			g[cu]=0;
			if(x>0)q.push_back((y*n)+x-1);
			if(y>0)q.push_back(((y-1)*n)+x);
			a++;
		}
	}
	std::cout<<a<<std::endl;
}

int main() {
	solve();
}
