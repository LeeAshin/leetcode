class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rsl = ""
        lst = s.split(" ")
        r = []
        str = " "
        for word in lst:
            rsl = word[::-1]
            r.append(rsl)
        return str.join(r)
