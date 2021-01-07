# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        totalSum = self.computeSum(l1, l2)

        returnList = ListNode(totalSum % 10)
        totalSum //= 10

        while totalSum:
            currentElem = totalSum % 10
            tempNode = ListNode(currentElem)
            if returnList.next == None:
                returnList.next = tempNode
            else:
                self.addToEnd(returnList, tempNode)

            totalSum //= 10


        return returnList


    # Travel both the numbers from right to left and add it to new node
    #newNode = ListNode()
    #
    #carry = 0
    #i = 0
    #while (l1 != None or l2 != None):
    #    first = l1.val if l1 != None else 0
    #    second = l2.val if l2 != None else 0
    #    current = first + second
    #    if carry:
    #        current += carry
    #    if current >= 10: 
    #        carry = current // 10
    #        current %= 10
    #        #carry = current % 10
    #        #current //= 10
    #    
    #    print(current, carry)
    #    if i == 0:
    #        newNode.val = current
    #        i += 1
    #    else:
    #        self.addToEnd(newNode, current)
    #    
    #    if(l1 == None): l2 = l2.next
    #    else: l1 = l1.next
    #    
    #return newNode

    def addToEnd(self, root, temp):
        if root.next == None:
            root.next = temp
        else:
            return self.addToEnd(root.next, temp)

    def computeSum(self, l1: ListNode, l2: ListNode) -> int:
        number1 = ''
        number2 = ''
        while l1.next != None:
            number1 += str(l1.val)
            l1 = l1.next
        number1 += str(l1.val)

        while l2.next != None:
            number2 += str(l2.val)
            l2 = l2.next
        number2 += str(l2.val)

        number1 = number1[::-1]
        number2 = number2[::-1]

        totalSum = int(number1) + int(number2)

        return totalSum
