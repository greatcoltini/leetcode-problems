class Solution(object):

    def is_valid(self, s):
        """

        :param s:
        :return:
        """
        bracket_order = []

        for bracket in s:
            if self.is_left(bracket):
                bracket_order.append(bracket)
            if self.is_right(bracket) and not bracket_order:
                return False
            elif self.is_right(bracket):
                temp = bracket_order.pop()
                if self.isOpposite(temp, bracket):
                    pass
                else:
                    return False

        if not bracket_order:
            return True
        else:
            return False


    def isOpposite(self, f_b, s_b):
        """
        :param s:
        :return:
        """
        if f_b == '(':
            return s_b == ')'
        elif f_b == '[':
            return s_b == ']'
        elif f_b == '{':
            return s_b == '}'
        else:
            return False


    def is_left(self, bracket):
        if bracket == '(' or bracket == '[' or bracket == '{':
            return True
        return False

    def is_right(self, bracket):
        if bracket == ')' or bracket == ']' or bracket == '}':
            return True
        return False


print(Solution().is_valid("()"))


