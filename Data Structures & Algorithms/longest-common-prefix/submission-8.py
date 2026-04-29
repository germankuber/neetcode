from typing import List


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        for index, letter in enumerate(strs[0]):
            for word in strs[1:]:
                if index >= len(word) or word[index] != letter:
                    return strs[0][:index]
        return strs[0] 