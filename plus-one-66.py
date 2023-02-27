class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        numbers_str = ""
        numbers_list = []
        
        # add to str

        for digit in digits:
            numbers_str += str(digit)
            
        number_int = int(numbers_str)
        
        number_int += 1
        
        numbers_str = str(numbers_int)
        
        for char in numbers_str:
            numbers_list.append(char)

        return numbers_list