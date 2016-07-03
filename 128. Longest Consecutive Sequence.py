"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


class Solution(object):
    # Time：O(n^2)
    # Space: O(n)
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = {}
        count = 0
        for i in nums:
            k = i
            if k not in temp:
                cnt = 1
                temp[k] = 1
                while (k + 1) in temp:
                    k += 1
                    cnt += 1
                    temp[k] = 1
                k = i
                while (k - 1) in temp:
                    k -= 1
                    cnt += 1
                    temp[k] = 1
                if cnt > count:
                    count = cnt
        return count


class Solution2(object):
    # Time: O(n)
    # Space: O(n)
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unions = {}
        maxlen = 0
        for n in nums:
            if unions.has_key(n):  # duplicate n, skip
                continue
            start = end = n
            if unions.has_key(n + 1):  # update end if has bigger neighbouring section
                end = unions[n + 1][1]
            if unions.has_key(n - 1):  # update start if has smaller neighbouring section
                start = unions[n - 1][0]
            unions[start] = unions[end] = unions[n] = (start, end)
            maxlen = max(end - start + 1, maxlen)
        return maxlen

if __name__ == '__main__':
    A = [100, 4, 200, 1, 3, 2]
    print Solution().longestConsecutive(A)
    print Solution2().longestConsecutive(A)
