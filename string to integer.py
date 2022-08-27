class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # create and initialize variables
        curr_item = ''
        int_list = ''
        index = 0
        positive = True
        length = len(s)

        # read in and ignore white space
        for item in s:
            if item == ' ':
                pass
            else:
                index = s.index(item)
                curr_item = item
                break

        # determine sign of integer
        if curr_item == '-':
            positive = False
            index += 1
        elif curr_item == '+':
            index += 1

        # form integer
        for i in range(index, length):
            if s[i] >= '0' and s[i] <= '9':
                int_list += s[i]
            else:
                break

        # if we do not find integers, return 0
        if not int_list:
            return 0

        # assign sign
        if positive:
            integer = int(int_list)
        else:
            integer = - int(int_list)

        # clamp the integer within the bounds
        if integer > (2**31 - 1):
            return (2**31 - 1)
        elif integer < (- 2**31):
            return - 2**31
        return integer

print(Solution().myAtoi("a0050"))
