class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        num2 = "1" * (len(bin(num)) - 2)
        return int(num2, 2) ^ num