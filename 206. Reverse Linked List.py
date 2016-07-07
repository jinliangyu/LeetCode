"""
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Time: O(n)
# Space: O(1)
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prv = None
        while head:
            n = head.next
            head.next = prv
            prv = head
            head = n
        return prv


# Time: O(n)
# Space: O(1)
# Iterative solution.
class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(float("-inf"))
        while head:
            # dummy.next, head.next, head = head, dummy.next, head.next
            if dummy.next:
                print dummy.next.val,
            if head:
                print head.val
        return dummy.next


# Time: O(n)
# Space: O(n)
# Recursive solution.
class Solution3(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


# Time: O(n)
# Space: O(n)
class Solution4(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        alist = []
        while head:
            alist.append(head.val)
            head = head.next
        if alist != []:
            newhead = ListNode(alist[-1])

            i = len(alist) - 2
            current = newhead
            while i >= 0:
                current.next = ListNode(alist[i])
                current = current.next
                i -= 1
            return newhead
        else:
            return head


if __name__ == '__main__':
    l, l.next, l.next.next, l.next.next.next = ListNode(2), ListNode(4), ListNode(3), ListNode(5)
    r = Solution2().reverseList(l)
    print r.val, r.next.val, r.next.next.val, r.next.next.next.val
