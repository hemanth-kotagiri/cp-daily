#include<iostream>
#include<bits/stdc++.h>

using namespace std;

bool reversed(string s, string t){
	if(s.length() != t.length()) return false;
	for(unsigned int i = 0; i < s.length(); i++){
		if(s[i] != t[s.length() - i - 1]) return false;
	}
	return true;
}


int main(){
	string s,t;
	cin >> s >> t;
	reversed(s, t) ? cout << "YES" : cout<<"NO";
		
}
