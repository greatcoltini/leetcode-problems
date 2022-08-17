class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        unique_chars = []
        current_highest = 0

        while counter < len(s):

            # traverse substring based on counter location
            for i in range(counter, len(s)):
                char = s[i]
                if char not in unique_chars:
                    unique_chars.append(char)
                else:
                    break

            if len(unique_chars) > current_highest:
                current_highest = len(unique_chars)
            unique_chars = []
            counter += 1

        # return the highest substring
        return current_highest

print(Solution().lengthOfLongestSubstring("jbpnbwwd"))