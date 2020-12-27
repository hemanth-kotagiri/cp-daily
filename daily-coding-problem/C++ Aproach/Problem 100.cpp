#include<iostream>
#include<math.h>
using namespace std;

bool isPrime(int n){
    if(n==2||n==3){
        return true;
    }
    for(int i = 2;i<pow(n,0.5)+1;i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}


main(){
    int n = 1234500006;
    for(int i =2;i<pow(n,0.5)+1;i++){
        if(isPrime(i)&& isPrime(abs(i-n))){
            cout<<i<<" "<<abs(i-n);
            break;
        }
    }
    return 0;
}
