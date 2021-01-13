#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){
	int n; cin >> n;
	map<string,int> shapes;
	shapes.insert(pair<string,int>("Tetrahedron",4));
	shapes.insert(pair<string,int>("Cube",6));
	shapes.insert(pair<string,int>("Octahedron",8));
	shapes.insert(pair<string,int>("Dodecahedron",12));
	shapes.insert(pair<string,int>("Icosahedron",20));
	int total = 0;
	while(n){
		string ans; cin >> ans;
		total += shapes[ans];
		n-=1;
	}
	cout << total;
}
