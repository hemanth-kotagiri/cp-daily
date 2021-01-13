#include<iostream>
#include<bits/stdc++.h>

using namespace std;

// achievement : space => O(1).


int main(){
	long n; cin >> n;
	
	vector<int> array;
	
	int segment = 0;
	int longest = 0;
	int a, b;
	for(int i = 0; i < n; i++){
		int temp; cin >> temp;
		if(i == 0){
			a = temp;
			segment++;
		}
		else if(i == 1){
			b = temp;
			segment++;
		}
		else{
			if(a + b == temp){
				if(segment == 0) segment += 3;
				else segment++;
			}
			else{
				if(segment > longest) longest = segment;
				segment = 0;
			}
			a = b;
			b = temp;
		}
	}
	if(segment > longest) longest = segment;
	cout << longest;
	
}
