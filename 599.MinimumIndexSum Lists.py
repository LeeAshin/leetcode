class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        result = []
        final = []
        r = []
        for w in list1:
            if w in list2:
                result.append(list1.index(w) + list2.index(w))
                result = sorted(result)
        for w in list1:
            if w in list2 and list1.index(w)+list2.index(w) == result[0]:
                final.append(w)
        return final