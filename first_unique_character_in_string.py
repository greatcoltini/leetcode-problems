

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # create our two lists
        unique = []
        non_unique = []

        # for each element in string, we determine its uniqueness
        for c in s:
            if c in non_unique:
                pass
            elif c in unique:
                non_unique.append(c)
                unique.remove(c)
            else:
                unique.append(c)

        # we return the first non-repeating character
        if unique:
            return s.index(unique[0])
        else:
            return -1


class Alt_sol(object):
    def firstUniqChar(self, s: str) -> int:
        l_dict = dict()
        uniquel_dict = dict()
        for l in s:
            if l not in l_dict.keys() and l not in uniquel_dict.keys():
                l_dict.update({l: 1})
                uniquel_dict.update({l: 1})
            elif l in uniquel_dict.keys() and l in l_dict.keys():
                l_dict.update({l: l_dict[l] + 1})
                del uniquel_dict[l]
            else:
                l_dict.update({l: l_dict[l] + 1})
        if uniquel_dict:
            return s.index(list(uniquel_dict.keys())[0])
        return -1