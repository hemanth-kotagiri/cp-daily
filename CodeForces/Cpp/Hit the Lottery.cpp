#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){
	int n, bills = 0;
	cin >> n;
	vector<int> coins;
	coins.push_back(100);
	coins.push_back(20);
	coins.push_back(10);
	coins.push_back(5);
	coins.push_back(1);
	vector<int>::iterator i;
	for(i = coins.begin(); i!=coins.end(); ++i){
		if(n >= *i){
			bills += n/(*i);
			n = n % (*i);
			if(n == 0) break;
		}
	}
	cout << bills;
	
}
