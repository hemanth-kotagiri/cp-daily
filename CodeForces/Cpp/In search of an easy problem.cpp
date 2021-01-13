#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){
	int n; cin >> n;
	int cur = 0;
	for(int i = 0; i < n; i++){
		int temp;
		cin >> temp;
		cur = max(temp,cur);
	}
	cur == 1 ? cout <<"HARD" : cout << "EASY";	
}
