# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        count = 0
        list_items = []
        while head:
            count += 1
            list_items.append(head.val)
            head = head.next
        reverse = reversed(list_items)

        for count, value in enumerate(reverse):
            if not value == list_items[count]:
                print(value)
                print(list_items[count])
                return False

        return True


palindrome = ListNode(3, ListNode(2, ListNode(3, None)))

print(Solution().isPalindrome(palindrome))
