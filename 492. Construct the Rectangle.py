class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        n = int(math.sqrt(area))
        while area%n != 0:
            n = n - 1
        return [area//n,n]