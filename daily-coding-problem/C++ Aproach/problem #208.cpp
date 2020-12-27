#include<iostream>
using namespace std;

class Node{
    public:
    	int val = 0;
    	Node next = Node(NULL);
        Node(int val, int next = Node(-1)){
            this->val = val;
            this->next = next;
        }
        
        void printer(){
        	if(this->next == NULL){
        		cout << this->val;
        		return;
			}
			cout << this->val << " --> ";
			return this->next->printer();
		}
};


int main(){
    Node t(20);
    t.printer();
    return 0;
}
