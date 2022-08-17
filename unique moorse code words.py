import string


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # initialization of required variables
        moorse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                       "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        transformations = []
        moorse_transformation = ""

        # add transformation to a list
        for word in words:

            # for each letter in the word, convert it to it's moorse code representation
            for letter in word:
                moorse_transformation += (moorse_code[string.lowercase.index(letter)])

            # check if item is a unique transformation
            if moorse_transformation not in transformations:
                transformations.append(moorse_transformation)

            # reset the transformation
            moorse_transformation = ""

        return len(transformations)
