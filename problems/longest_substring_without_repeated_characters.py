# Problem link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    #abcabcbb
    def lengthOfLongestSubstring(self, s: str) -> int:

        myUniqueSet = set()
        longestSubstring = 0
        leftIndex = 0

        for character in s:
            if (character not in myUniqueSet):
                myUniqueSet.add(character)
            else:
                longestSubstring = max(longestSubstring, len(myUniqueSet))
                
                # Remove the string from the left until the set is unique again
                while (leftIndex < len(s)) and (character in myUniqueSet):
                    myUniqueSet.remove(s[leftIndex])
                    leftIndex = leftIndex + 1

                myUniqueSet.add(character)

        longestSubstring = max(longestSubstring, len(myUniqueSet))
        return longestSubstring