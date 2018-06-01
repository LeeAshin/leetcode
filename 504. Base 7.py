class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = 0
        rsl = ''
        if num == 0:
            return "0"
        anum = abs(num)
        while anum != 0:
            res = anum % 7
            anum = anum // 7
            rsl = str(res) + rsl
        if num >= 0:
            return rsl
        else:
            return "-" + rsl