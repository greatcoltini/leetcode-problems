
def maxVowels(s, k):
    """
    :type s: str, the entire string
    :type k: int, the length of the substring
    :rtype: int, the max vowels in any substring of size k
    """
    # brute force method: go through string one char at a time
    # from set char, create string from s[char:k], check number of vowels
    max_vowels = 0
    counter = 0
    while counter < len(s) - 1:
        current_max = 0
        test_str = s[counter:counter+k]
        for letter in test_str:
            if isVowel(letter):
                current_max += 1
        if current_max > max_vowels:
            max_vowels = current_max
        current_max = 0
        counter += 1
    return max_vowels

def isVowel(char):
    """
    :type char: letter
    :rtype: bool, if the given char is a vowel
    """
    vowels = ["a", "e", "i", "o", "u"]
    
    return (char in vowels)


# alt soln
# keep window of size k; maintain # of vowels inside
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Build the window of size k, count the number of vowels it contains.
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count
        
        # Slide the window to the right, focus on the added character and the
        # removed character and update "count". Record the largest "count".
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i - k] in vowels)
            answer = max(answer, count)
        
        return answer


print(maxVowels("alliigator", 4))