class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        

        while num / 10 >= 1:
            num = self.adder(num)
        return num
            
            
            
    def adder(self, num):
        # strat is to break it into individual digits, add them all
        new_num = str(num)
        new_tot = 0
        for char in new_num:
            new_tot = new_tot + int(char)
        return new_tot