# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Remove Duplicates from Sorted List 83
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        if head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
                self.deleteDuplicates(head)
            else:
                self.deleteDuplicates(head.next)
        return head
                