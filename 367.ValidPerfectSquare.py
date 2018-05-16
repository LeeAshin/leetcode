class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if int(num ** 0.5) * int(num ** 0.5) == num:
            return True
        else:
            return False
