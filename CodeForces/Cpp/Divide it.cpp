#include<iostream>
#include<bits/stdc++.h>
#include<limits>

using namespace std;

bool comp(int a, int b) 
{ 
    return (a < b); 
} 
// greedy, we want to minimize the value n to be 1.

int min_moves(long long int n){
	int count = 0;
	long long int inf = 1000000000000000000;
	long long int two = inf, three = inf, five = inf;
	while(n!=1){
		if(n%2==0){
			two = n/2;
			//cout << two << endl;
		}
		if(n%3 == 0){
			three = 2*n/3;
			//cout << three << endl;
		}

		if(n%5 == 0){
			five = 2*n/5;
			//cout << five << endl;
		}
		
		long long int optimal = min(two,min(three,five));
		
		n = optimal;
		//cout << n << endl;
		count++;
	}
	return count;
	
}


int main(){
	cout << min_moves(10);
	
}
