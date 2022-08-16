import math

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    # create string of int, and reverse it
    s_x = str(x)
    r_s_x = s_x[::-1]

    # compare reverse string to original string; if difference we break
    for i in range(0, len(s_x)):
        char = s_x[i]
        r_char = r_s_x[i]
        if not char == r_char:
            return False
    return True

def findDigits(x):
    """

    :param x:
    :return: digits
    """
    if x > 0:
        digits = int(math.log10(x)) + 1
    elif x == 0:
        digits = 1
    elif x < 0:
        digits = int(math.log10(-x)) + 2
    return digits

def firstDigit(x):
    while x >= 10:
        x = x // 10
    return x

def isPalindromeInt(x):
    """

    :param x: int -- integer to check if is palindrome
    :return: True if palindrome // False if not
    """
    #
    # get the digits of the function
    num_mods = findDigits(x)
    print(num_mods)
    middle = num_mods // 2
    counter = 1

    while counter <= middle:
        compare_front = x // (10 ** (middle - counter))
        compare_back = x % (num_mods * counter)
        print(compare_front)
        print(compare_back)

        if compare_front != compare_back:
            return False
        else:
            counter += 1
    return True

print(isPalindromeInt(121))

