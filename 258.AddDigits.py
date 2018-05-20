class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        snum = str(num)
        while len(snum) != 1:
            rsl = 0
            for w in snum:
                rsl += int(w)
            snum = str(rsl)

        return int(snum)