#include <iostream>
#include <bits/stdc++.h>

void solve() {
	int w,h,n,m,x[1001]={0},y[1001]={0},xl=0,yl=0,xc,yc;
	std::cin>>w;
	std::cin>>h;
	std::cin>>n;
	std::cin>>m;
	for(int i=0;i<n;i++){
		std::cin>>xc;
		x[i]=xc-xl;
		xl=xc;
	}
	for(int i=0;i<m;i++){
		std::cin>>yc;
		y[i]=yc-yl;
		yl=yc;
	}
	x[n]=w-xc;
	y[m]=h-yc;
	n++;m++;
	std::sort(x,x+n);
	std::sort(y,y+m);
	std::cout<<x[n-1]*y[m-1]<<' ';
	std::cout<<((x[n-2]*y[m-1])>(x[n-1]*y[m-2])?(x[n-2]*y[m-1]):(x[n-1]*y[m-2]))<<std::endl;
}

int main() {
	solve();
}
