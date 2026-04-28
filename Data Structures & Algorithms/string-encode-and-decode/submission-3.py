import heapq
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_data = ""
        for item in strs:
            encoded_data += str(len(item)) + "#" + item 

        return encoded_data

    def decode(self, s: str) -> List[str]:
        count = 0
        result = []
        word = ""
        read_length = True
        length_concat = ""
        length = None
        for item in s:
            
            if read_length:
                if item == "#":
                    length = int(length_concat)
                    length_concat = ""
                    read_length = False
                else:
                    length_concat += item
                    
                if length == 0:
                    result.append("")
                    read_length = True
                    length = None
                    continue
                
            else:
                count += 1
                word += item
                if count == length:
                    result.append(word)
                    word = ""
                    length = None
                    read_length = True
                    count = 0
        return result
            