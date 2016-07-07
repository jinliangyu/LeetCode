"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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


# Time: O(n^2)
# Space: O(1)
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        current = dummy
        while head and head.next:
            if head.val != head.next.val:
                current.next = ListNode(head.val)
                current = current.next
            else:
                while head.next and head.val == head.next.val:
                    head = head.next
            head = head.next
        if head:
            current.next = ListNode(head.val)
        return dummy.next


# Time: O(n)
# Space: O(1)
class Solution2(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        current = head
        d = {}
        l = []
        while current:
            if current.val not in d:
                d[current.val] = 1
                l.append(current.val)
            else:
                d[current.val] += 1
            current = current.next
        current = dummy
        for i in l:
            if d[i] == 1:
                current.next = ListNode(i)
                current = current.next
        return dummy.next


if __name__ == '__main__':
    head = createLinkList([1, 2, 3, 3, 4, 4, 5])
    # head = createLinkList([1, 1, 1, 2, 3])
    # head = createLinkList([1, 1])
    print Solution2().deleteDuplicates(head)
