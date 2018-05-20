class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        R = []
        M = []
        for a in A:
            a = list(reversed(a))
            for num in a:
                num = num ^ 1
                M.append(num)
            R.append(M)
            M = []
        return R