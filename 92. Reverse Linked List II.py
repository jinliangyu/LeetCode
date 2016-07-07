# -*- coding:utf-8 -*-
"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self:
            return "{} -> {}".format(self.val, str(self.next))


# Time: O(n)
# Space: O(1)
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(float("-inf"))
        dummy.next = head
        prev = dummy
        for i in xrange(m - 1):
            prev = prev.next
        newhead = prev
        prev = newhead.next
        current = prev.next
        for i in xrange(m, n):
            prev.next = current.next
            current.next = newhead.next
            newhead.next = current
            current = prev.next
        return dummy.next


# Time: O(n)
# Space: O(1)
class Solution2(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        diff, dummy, cur = n - m + 1, ListNode(-1), head
        dummy.next = head

        last_unswapped = dummy
        while cur and m > 1:
            cur, last_unswapped, m = cur.next, cur, m - 1

        prev, first_swapped = last_unswapped, cur
        while cur and diff > 0:
            cur.next, prev, cur, diff = prev, cur, cur.next, diff - 1

        last_unswapped.next, first_swapped.next = prev, cur

        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print head
    print "After Reverse ↓"
    print Solution2().reverseBetween(head, 2, 4)
