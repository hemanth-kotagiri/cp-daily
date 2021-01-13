#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){
	int n; cin >> n;
	string stones; cin >> stones;
	stack <char> s;
	int count = 0;
	
	for(unsigned int i = 0; i < stones.length(); i++){
		if(s.empty()) s.push(stones[i]);
		else{
			if(s.top() == stones[i]){
				s.pop();
				count++;
				s.push(stones[i]);
			}
			else{
				s.push(stones[i]);
			}
		}
	}
	cout << count;
}
