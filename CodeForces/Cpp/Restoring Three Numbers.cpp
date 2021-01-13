#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){
	// a+b, a+c, b+c and a+b+c
	// a+c - b+c = a - b
	// a + b + (a+c - b+c) = 2*a
	vector<int>a;
	for(int i = 0; i < 4; i++){
		int temp = 0;
		cin >> temp;
		a.push_back(temp);
	}
	sort(a.begin(), a.end());
	cout << a[3] - a[0] << " " << a[3] - a[1] << " " << a[3] - a[2] << endl;
	//cin >> x >> y >> z >> total;
	//int a = total - z;
	//int b = total - y;
	//int c = total - x;
	
}
