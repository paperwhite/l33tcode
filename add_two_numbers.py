# Definition for singly-linked list.
#class ListNode(object):
##    def __init__(self, x):
#        self.val = x
#       self.next = None

class Solution(object):
    def carryCheck(self, x, y):
        tmp = x+y
        if (tmp>=10):
            car=1
            sum=tmp%10
        else:
            car=0
            sum=tmp
        return(sum,car)
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2
        sum1 = 0
        head_res = ListNode(-1)
        tail = head_res
        carry = 0
        while ptr1 is not None or ptr2 is not None:
            if(ptr1 is None):
                if head_res.val==-1:
                    head_res.next=None
                    tail = head_res
                    head_res.val=ptr2.val
                else:
                    l4 = ListNode(None)
                    tail.next =l4
                    tail=l4
                    l4.val,carry = self.carryCheck(ptr2.val,carry)
                ptr2 = ptr2.next
                
            elif(ptr2 is None):
                if head_res.val==-1:
                    head_res.next=None
                    tail = head_res
                    head_res.val=ptr1.val
                else:
                    l4 = ListNode(None)
                    tail.next=l4
                    tail=l4
                    l4.val,carry = self.carryCheck(ptr1.val,carry)
                ptr1 = ptr1.next
            else:
                if head_res.val==-1:
                    head_res.next=None
                    tail = head_res
                    head_res.val,carry = self.carryCheck(ptr1.val+ptr2.val,carry)
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next
                else:
                    l4 = ListNode(None)
                    tail.next  = l4
                    l4.val,carry = self.carryCheck(ptr1.val+ptr2.val,carry)
                    tail=l4
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next
        if carry == 1:
            l4 = ListNode(None)
            tail.next  = l4
            l4.val=carry        
        return head_res
                
