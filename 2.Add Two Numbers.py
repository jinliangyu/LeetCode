"""
You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ""
        num2 = ""
        while l1 is not None:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2 is not None:
            num2 = str(l2.val) + num2
            l2 = l2.next
        result = str(int(num1) + int(num2))[::-1]
        dummyHead = ListNode(0)
        current = dummyHead
        for i in range(len(result)):
            current.next = ListNode(int(result[i]))
            current = current.next
        return dummyHead.next


class Solution2(object):
    # Time: O(max(m, n))
    # Space: O(max(m, n))
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(0)
        carry, current = 0, dummyHead
        while l1 or l2:
            sum = carry
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry = sum / 10
            current.next = ListNode(sum % 10)
            current = current.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummyHead.next


def main():
    l1, l1.next, l1.next.next = ListNode(2), ListNode(4), ListNode(3)
    l2, l2.next, l2.next.next = ListNode(5), ListNode(6), ListNode(4)

    L = Solution().addTwoNumbers(l1, l2)
    print "# Solution1:"
    print "l1\t\t=","{0} -> {1} -> {2}".format(l1.val, l1.next.val, l1.next.next.val)
    print "l2\t\t=","{0} -> {1} -> {2}".format(l2.val, l2.next.val, l2.next.next.val)
    print "l1+l2 \t=","{0} -> {1} -> {2}".format(L.val, L.next.val, L.next.next.val)
    print "# Solution2:"
    L = Solution2().addTwoNumbers(l1, l2)
    print "l1\t\t=","{0} -> {1} -> {2}".format(l1.val, l1.next.val, l1.next.next.val)
    print "l2\t\t=","{0} -> {1} -> {2}".format(l2.val, l2.next.val, l2.next.next.val)
    print "l1+l2 \t=","{0} -> {1} -> {2}".format(L.val, L.next.val, L.next.next.val)

if __name__ == '__main__':
    main()
