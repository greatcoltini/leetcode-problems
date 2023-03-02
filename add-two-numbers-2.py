# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # check if next; four cases:
        #  1. neither have next, 2. both have next, 3/4. one has next
        if l1.next == None and l2.next == None:
            if (l1.val + l2.val > 10):
                return ListNode((l1.val + l2.val) % 10, 1)
            return ListNode(l1.val + l2.val)
        elif l1.next != None and l2.next != None:
            if (l1.val + l2.val >= 10):
                return ListNode(ListNode((l1.val + l2.val) % 10), self.addTwoNumbers(l1.next, l2.next))
            return ListNode(ListNode(l1.val + l2.val), self.addTwoNumbers(l1.next, l2.next))
        elif l1.next != None:
            return ListNode(ListNode(l1.val + l2.val), l1.next)
        elif l2.next != None:
            return ListNode(ListNode(l1.val + l2.val), l2.next)
        else:
            return None
        