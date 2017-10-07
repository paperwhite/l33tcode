"""
@author: Shibani
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # create two pointers and separate them at a distance of n
        ptr1 = head

        if n == 1 and head.next == None:
            head = None
            return head
        elif n==1:
            while (ptr1.next).next != None:
                ptr1 = ptr1.next
            ptr1.next = None
            print ptr1.val
            return head
        count = 1
        ptr2=head
        while count !=n:
            ptr2 = ptr2.next
            count = count+1

        # maintain the distance till the second pointer reaches the end of the list   
        while ptr2.next!= None:
            ptr2 = ptr2.next
            par = ptr1
            ptr1 = ptr1.next

        # the parent node is the parent of the node to be removed    
        if ptr1 != head:
            par.next = (ptr1.next)
        # if it is the head node that has to be removed, move the head to the next node
        else:
            head = ptr1.next
        return head
        
