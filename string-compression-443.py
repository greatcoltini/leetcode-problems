class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        #  begin with empty string
        s = ""
        current_char = ""
        current_grp = 0

        for char in chars:
            # if group continuing
            if char == current_char:
                current_grp += 1
            else:
                if current_grp > 1:
                    s += current_char
                    s += str(current_grp)
                    current_char = char
                    current_grp = 1
                elif current_grp == 1:
                    s += current_char
                    current_char = char
                    current_grp = 1
                else:
                    current_grp = 1
                    current_char = char
        # perform for final chars
        if (current_grp > 1):
            s += current_char
            s += str(current_grp)
        else:
            s += current_char


        arr_s = list(s)

        counter = 0
        for char in arr_s:
            chars[counter] = char
            counter += 1

        return len(s)