#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){
	int cap = 0, n, exit, enter, curr = 0, i;
	cin >> n;
	i = n;
	
	while(i){
		if(i == n){
			cin >> exit >> enter;
			curr = cap = enter;
			i--;
			continue;
		}
		cin >> exit >> enter;
		curr -= exit;
		curr += enter;
		if(curr > cap) cap = curr;
		i--;
	}
	cout << cap;
}
