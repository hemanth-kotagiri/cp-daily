#include<iostream>
#include<bits/stdc++.h>

using namespace std;

bool unique(int n){
	map<int,int>mapper;
	while(n){
		int curr = n%10;
		if(mapper.empty()){
			mapper[curr] = 1;
		}
		else{
			if(mapper[curr] == 1) return false;
			mapper[curr] = 1;
		}
		n /= 10;
	}
	return true;
}


int main(){
	int n; cin >> n;
	while(true){
		n += 1;
		if(unique(n)){
			cout << n;
			break;
		}
	}
}
