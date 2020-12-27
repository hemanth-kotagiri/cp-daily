# Medium.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def printer(self):
        if self.next == None:
            print(self.val)
            return
        print(f"{self.val} -- > ", end = '')
        return self.next.printer()


# latest approach
def add_to_beg(node, val):
    if node.val == '-inf':
        node.val = val
        return node
    else:
        newNode = Node(val)
        newNode.next = node
        return newNode

def add_to_end(ll, val):
    if ll.next == None:
        ll.next = Node(val)
        return ll
    return add_to_end(ll.next, val)


#5 -> 1 -> 8 -> 0 -> 3
def Sol(ll, k, newll=Node('-inf'), count=0):
    if ll.val < k:
        newll = add_to_beg(newll, ll.val)
    elif ll.val > k:
        add_to_end(newll, ll.val)
    else:
        count += 1
        if ll.next == None:
            for i in range(count):
                add_to_end(newll, k)
            return newll
    return Sol(ll.next, k, newll, count)

#5 -> 1 -> 8 -> 0 -> 3
# Node(1,Node(4,Node(3,Node(2,Node(5,Node(2,Node(3))))))) ==  1->4->3->2->5->2->3
GivenLL = Node(5, Node(1, Node(8, Node(0, Node(3)))))
k = 3


Sol(GivenLL,k).printer()

exit()

# First approach

def convertToList(LinkedList,valList = []):
    if LinkedList.next != None:
        valList.append(LinkedList.val)
        return convertToList(LinkedList.next, valList)
    valList.append(LinkedList.val)
    return valList

def order(values, k):
    answer = []
    count  = 0
    for i in range(len(values)):
        curr_elemt = values[i]
        if curr_elemt < k:
            answer.insert(0, curr_elemt)
        elif curr_elemt > k:
            answer.append(curr_elemt)
        else:
            count += 1
    for i in range(count):
        answer.append(k)
    return answer

def add_to_end(ll, val):
    if ll.next == None:
        ll.next = Node(val)
        return ll
    return add_to_end(ll.next, val)


def toLL(LL,k):
    values = order(convertToList(LL),k)
    NewLL = Node(values[0])
    for i in range(1,len(values)):
        add_to_end(NewLL, values[i])
    return NewLL

a = toLL(GivenLL,k)

a.printer()
