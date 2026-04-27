from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result:dict[tuple, list] = {}
        for word in strs:
            list_id = [0] * 26
            for letter in word:
                list_id[ ord(letter)- ord("a")] += 1
            id = tuple(list_id)
            if id not in result:
                result[id] = []
            
            result[id].append(word)
                
        
        return list(result.values())