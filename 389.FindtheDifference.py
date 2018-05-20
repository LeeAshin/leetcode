class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sint = 0
        tint = 0
        for word in s:
            sint += ord(word)
        for word in t:
            tint += ord(word)
        return chr(tint-sint)