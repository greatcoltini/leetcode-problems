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
        
        numbers_str = str(number_int)
        
        for char in numbers_str:
            numbers_list.append(int(char))

        return numbers_list
    
    
# class Solution(object):
    
# def plusOne(digits):
#         num_int = 0
#         i = 1
        
#         for digit in digits:
#             num_int += digit ** (len(digits) - i)
#             i += 1
            
#         print(num_int)
        
#         num_int += 1
#         digits_altered = []
        
#         while num_int > 0:
#             digits_altered.append(num_int % 10)
#             num_int = num_int // 10
        
#         return digits_altered

# print(plusOne([1, 2, 3]))