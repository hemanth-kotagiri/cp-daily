#include<iostream>

using namespace std;

int main(){
	int n,k;
	cin >> n >> k;
	for(int i = 0; i < k; i++){
		n%10==0 ? n/=10 : n--;
	}
	cout << n;
	
}
