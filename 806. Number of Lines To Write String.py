class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        len = 0
        lines = 1

        for word in S:
            x = ord(word) - 97
            len += widths[x]
            if len > 100:
                lines += 1
                len = widths[x]
        return [lines, len]