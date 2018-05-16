class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        s = 1
        for i in range(1,n+1):
            s = s*i
        seq = str(s)
        for word in seq[::-1]:
            if word == "0":
                count += 1
            else:
                break
        return count