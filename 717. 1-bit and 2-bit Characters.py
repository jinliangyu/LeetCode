"""
We have two special characters. The first character can be represented by one
bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last
character must be a one-bit character or not. The given string will always end
with a zero.
"""


class Solution1(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1
        return i == len(bits) - 1


class Solution2(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        parity = bits.pop()
        while bits and bits.pop():
            parity ^= 1
        return parity == 0


if __name__ == '__main__':
    bits = [1, 0, 0]
    # bits = [1, 1, 1, 0]
    print Solution1().isOneBitCharacter(bits)
    print Solution2().isOneBitCharacter(bits)
