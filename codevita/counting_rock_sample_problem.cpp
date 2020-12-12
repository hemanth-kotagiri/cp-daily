#include<bits/stdc++.h>
using namespace std;


int main() {
    long R, S, i;
    cin >> S >> R;
    vector<int> sizes, accepts;
    vector<pair<long, long>> ranges;
    for(i = 0; i < S; i++) {
        long curr;
        cin >> curr;
        sizes.push_back(curr);
    }
    for(i = 0; i < R; i++) {
        //TODO: How the freak to push_back the goddamn pair.
        long l1, l2;
        cin >> l1 >> l2;
        ranges.push_back(make_pair(l1, l1));
    }
    for(auto size : sizes) {
        for(i = 0; i < R; i++) {
            if(ranges[i][0] < size < ranges[i][1]) accepts[i] = accepts[i] + 1;
        }
    }
    for(auto accept : accepts) {
        cout << accept << endl;
    }
}
