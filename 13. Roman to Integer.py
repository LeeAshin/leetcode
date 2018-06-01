class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num_list = [dictionary.get(x) for x in s]
        total = 0
        for index, num in enumerate(num_list):
            if max(num_list[index:]) <= num:
                total += num
            else:
                total -= num
        return total