#1290. Convert Binary Number in a Linked List to Integer

# Given head which is a reference node to a singly-linked list. 
# The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binaryNumber = 0
        while(head != None):
            curr = head.val
            binaryNumber = binaryNumber * 10 + curr
            head = head.next

        return int(str(binaryNumber), 2)
