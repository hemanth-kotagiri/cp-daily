#include<iostream>
#include<bits/stdc++.h>

using namespace std;

// time limit exceeded.


bool isPal(long long int n){
	long long int temp = n, i = 0, even = 0;
	while(n){
		i = i*10 + n%10;
		n/=10;
		even++;
	}
	return (temp == i && even%2==0);
} 

int main(){
	long long int n; cin >> n;
	long long int number = 11;
	while(n){
		if(isPal(number)){
			n--;
		}
		if(n!=0) number++;
	}
	cout << number;
}
