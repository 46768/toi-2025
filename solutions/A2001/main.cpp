#include <iostream>

int count(int *m, int *a, int ml, int al){
	int mi=0,ai=0,c=0;

	while(mi<ml){
		if(a[ai]==m[mi])c++;
		if((al-ai)==1)break;
		if(a[ai+1]<=m[mi]){
			c++;
			ai++;
		}else{
			mi++;
		}
	}

	return c;
}

void solve() {
	int rl,bl;
	int r[501],b[501];
	std::cin>>rl;
	std::cin>>bl;
	
	r[0]=0;b[0]=0;
	for(int i=0;i<rl;i++){
		std::cin>>r[i+1];
	}
	for(int i=0;i<bl;i++){
		std::cin>>b[i+1];
	}
	int rmba=count(r,b,rl,bl);
	int bmra=count(b,r,bl,rl);
	std::cout<<(((bmra-rmba)/2)+rmba-(rl==bl))<<std::endl;
}

int main() {
	solve();
}
