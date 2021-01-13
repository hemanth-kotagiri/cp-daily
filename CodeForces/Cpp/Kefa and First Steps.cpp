#include<bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define ll long long

int main(){
		ll n ,count = 0, f = 0; cin >> n;
		int money[n];
		for(ll i = 0; i < n; i++){
			scanf("%d",&money[i]);
		}
		
		for(ll i = 0; i < n; i++){
			if(money[i] >= money[i-1]) count ++;
			else f = max(f,count), count = 1;
		}
		f = max(count,f);
		cout << f;
		
		//while(i!=n){
		//	int curr_mon = money[i];
			//cout << "Now money: "<<curr_mon << endl;
		//	if(count == 0) count++;
			//else{
				//if(curr_mon >= prev_mon) count++;
				//else{
					//if(count > f){f = count; count = 1;}
				//}
			//}
			//prev_mon = curr_mon;
			//cout << "count : " << count << " F " << f << endl; 
			//i++;
		//}
		//if(count > f) f = count;
		//cout << f;
}
