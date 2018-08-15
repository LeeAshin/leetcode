class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for w in s:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        for w in s:
            if d[w] == 1:
                return s.find(w)
            else:
                continue
        return -1