"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
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


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head
        length = 1
        p = head
        while p.next:
            length += 1
            p = p.next
        k = length - k % length
        p.next = head
        for i in xrange(k):
            p = p.next
        head = p.next
        p.next = None
        return head


if __name__ == '__main__':
    head = createLinkList([1, 2, 3, 4, 5])
    # head = createLinkList([1, 2])
    print Solution().rotateRight(head, 2)
