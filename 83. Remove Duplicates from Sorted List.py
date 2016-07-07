"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


def createLinkList(alist):
    dummy = ListNode(0)
    current = dummy
    for i in alist:
        current.next = ListNode(i)
        current = current.next
    return dummy.next


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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        pre = float("-inf")
        current = dummy
        while head:
            if head.val > pre:
                current.next = ListNode(head.val)
                pre = head.val
                current = current.next
            head = head.next
        return dummy.next


class Solution2(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while current:
            runner = current.next
            while runner and runner.val == current.val:
                runner = runner.next
            current.next = runner
            current = runner
        return head


class Solution3(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr!=None and curr.next!=None:
            if (curr.val == curr.next.val):
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


if __name__ == '__main__':
    head = createLinkList([1, 1, 2, 3, 3])
    print Solution2().deleteDuplicates(head)