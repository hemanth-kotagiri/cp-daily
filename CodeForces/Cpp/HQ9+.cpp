#include<iostream>
#include<bits/stdc++.h>
#include<limits>

using namespace std;

int main(){
	string input; cin >> input;
	vector<char> valid;
	valid.push_back('H');
	valid.push_back('Q');
	valid.push_back('9');
	//valid.push_back('+');
	
	bool temp = false;
	
	for(unsigned int i = 0; i < input.length(); i++){
		for(int k = 0; k < 4; k++){
			//cout << valid[k];
			if(valid[k] == input[i]) temp = true;
		}
		if(temp){
			cout << "YES";
			exit(0);
		}
	}
	cout << "NO";
}
