# Ref : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) > len(haystack) :
            return -1

        if needle == haystack:
            return 0

        characterPositionDict = { }
        for i in range(0, len(haystack)):
            if haystack[i] not in characterPositionDict:
                characterPositionDict[haystack[i]] = []
            
            characterPositionDict[haystack[i]].append(i)

        needlePositionDict = {}
        for i in range(0, len(needle)):
            if needle[i] not in needlePositionDict:
                needlePositionDict[needle[i]] = []
            
            needlePositionDict[needle[i]].append(i)            
        
        for character in needlePositionDict.keys():
            if character not in characterPositionDict:
                return -1

        found = False
        foundIndex = -1
        for i in range(0, len(needle)):

            needleCharacter = needle[i]
            if needleCharacter in characterPositionDict:
                characterPositions = characterPositionDict[needleCharacter]

                for pos in characterPositions:
                    stringToCompareInHaystack = haystack[pos: pos+len(needle)]
                    if ( stringToCompareInHaystack == needle ):
                        found = True
                        foundIndex = pos
                        break
                    else:
                        found = False
            
            if found:
                break

        return foundIndex

        
