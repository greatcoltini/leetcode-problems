class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # cases: IV or IX -> 4 and 9 resp.
        # cases: XL or XC -> 40 and 90 resp.
        # cases: CD and CM -> 400 and 900 resp.

        # I -> 1 ; V -> 5; X -> 10; L -> 50; C -> 100; D -> 500; M -> 1000

        number = 0
        counter = 0

        while counter < len(s):
            if s[counter] == 'M':
                number += 1000
            elif s[counter] == 'D':
                number += 500
            elif s[counter] == 'C':
                if counter < len(s) - 1:
                    if s[counter + 1] == 'D':
                        number += 400
                        counter += 1
                    elif s[counter + 1] == 'M':
                        number += 900
                        counter += 1
                    else:
                        number += 100
                else:
                    number += 100
            elif s[counter] == 'L':
                number += 50
            elif s[counter] == 'X':
                if counter < len(s) - 1:
                    if s[counter + 1] == 'L':
                        number += 40
                        counter += 1
                    elif s[counter + 1] == 'C':
                        number += 90
                        counter += 1
                    else:
                        number += 10
                else:
                    number += 10
            elif s[counter] == 'V':
                number += 5
            elif s[counter] == 'I':
                if counter < len(s) - 1:
                    if s[counter + 1] == 'V':
                        number += 4
                        counter += 1
                    elif s[counter + 1] == 'X':
                        number += 9
                        counter += 1
                    else:
                        number += 1
                else:
                    number += 1

            counter += 1
            
        return number