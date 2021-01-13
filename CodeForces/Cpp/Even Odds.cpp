#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
	ll n,k; cin >> n >> k;
	cout << n/2<<endl;
	if(k <= n/2){
		for(ll i = 1; i <= n; i++){
			if(i%2!=0){ k--; }
			if(k==0){cout << i; break;}
		}
	}
	else{
		k -= n/2;
		cout << k;
		for(ll i = 0; i <= n; i++){
			if(i%2==0){k--; }
			if(k==0){
				if(i == 0) cout << i+2;
				else cout << i;  
				break;
			}
		}
	}
}
