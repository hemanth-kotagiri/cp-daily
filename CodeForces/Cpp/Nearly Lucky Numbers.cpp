#include<bits/stdc++.h>
 
using namespace std;
 
bool isLucky(int n){
	if (n%4==0 || n%7==0) return true;
	while(n){
		int temp = n%10;
		if(temp == 4 || temp == 7) n/=10;
		else return false;
	}
	return true;
}
 
int main(){
	int n; cin >> n;
	if(isLucky(n)) cout << "YES"<<endl;
	else{
		for(int i = 1; i < n; i++){
			if(n%i==0 && isLucky(i)){cout << "YES: "<< i <<endl; exit(0);}
		}
		cout << "NO"<<endl;
	}
}
