# -*- coding:utf-8 -*-
"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""
import math


# Time: O(n)
# Space: O(1)
# Cantor expansion
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seq, k, fact = "", k - 1, self.factorial(n - 1)
        perm = [i for i in xrange(1, n + 1)]
        for i in reversed(xrange(n)):
            curr = perm[k / fact]
            seq += str(curr)
            perm.remove(curr)
            if i > 0:
                k %= fact
                fact /= i
        return seq


# Time: O(n)
# Space: O(1)
# Cantor expansion
class Solution2(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        init, k, fact = range(1, n + 1), k - 1, self.factorial(n - 1)
        seq = ""
        for i in range(n):
            temp = init[k / fact]
            seq += str(temp)
            init.remove(temp)
            if i < n - 1:
                k %= fact
                fact /= n - i - 1
        return seq


    def factorial(self, n):
        if n < 1:
            return 1
        else:
            return n * self.factorial(n - 1)

# Time limit exceeded!! TLE
class Solution3(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        init = range(1, n + 1)
        res = ""
        for i in range(1, k):
            self.nextPermutation(init)
        for i in init:
            res += str(i)
        return res

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k, l = -1, 0
        for i in xrange(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                k = i
        if k == -1:
            nums.reverse()
            return
        for i in xrange(k + 1, len(nums)):
            if nums[i] > nums[k]:
                l = i
        nums[k], nums[l] = nums[l], nums[k]
        nums[k + 1:] = nums[:k:-1]



if __name__ == '__main__':
    n = 3
    k = 3
    print Solution2().getPermutation(9, 171669)
    # print Solution().factorial(6)
