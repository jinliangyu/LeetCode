"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution(object):
    # Time: O(m + n)
    # Space: O(m + n)
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        nums = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < len(nums1):
            nums += nums1[i:]
        else:
            nums += nums2[j:]
        if len(nums) % 2 == 0:
            return (nums[len(nums) / 2] + nums[len(nums) / 2 - 1]) / 2.0
        else:
            return nums[len(nums) / 2]

    def getKth(self, A, B, k):
        lenA = len(A)
        lenB = len(B)
        if lenA > lenB: return self.getKth(B, A, k)
        if lenA == 0: return B[k - 1]
        if k == 1: return min(A[0], B[0])
        pa = min(k / 2, lenA)
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)

    # Time: O(log(m + n))
    # Space: O(log(m + n))
    def findMedianSortedArrays2(self, A, B):
        lenA = len(A)
        lenB = len(B)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(A, B, (lenA + lenB) / 2 + 1)
        else:
            return (self.getKth(A, B, (lenA + lenB) / 2) + self.getKth(A, B, (lenA + lenB) / 2 + 1)) * 0.5


class Solution2(object):
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        total =  m + n
        if total % 2 == 1:
            return self.find_kth(A, m, B, n, total / 2 + 1)
        else:
            return 0.5 * (self.find_kth(A, m, B, n, total / 2) +
                          self.find_kth(A, m, B, n, total / 2 + 1))


    def find_kth(self, A, m, B, n, k):
        if m > n:
            return self.find_kth(B, n, A, m, k)
        if m == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])
        ia = min(k / 2, m)
        ib = k - ia
        if A[ia - 1] < B[ib - 1]:
            return self.find_kth(A[ia:], m - ia, B, n, k - ia)
        elif A[ia - 1] > B[ib - 1]:
            return self.find_kth(A, m, B[ib:], n - ib, k - ib)
        else:
            return A[ia - 1]


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print Solution2().findMedianSortedArrays(nums1, nums2)
