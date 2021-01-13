#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){
	int n; cin >> n;
	int i = 0;
	if(n==1) cout <<"I hate it";
	else{
		while(i!=n){
			if(i%2==0){
				cout << "I hate ";
				if(i == n-1){
					cout << "it";
					break;
				}
				else{
					cout <<"that ";
				}
			}
			else{
				cout << "I love ";
				if(i == n-1){
					cout << "it";
					break;
				}
				else{
					cout <<"that ";
				}
			}
			i++;
		}
	}
}
