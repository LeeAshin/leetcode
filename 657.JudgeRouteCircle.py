class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up = moves.count("U")
        down = moves.count('D')
        left = moves.count('L')
        right = moves.count('R')

        if left == right and up==down:
            return True
        else:
            return False