import heapq
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_data = ""
        for item in strs:
            encoded_data += str(len(item)) + "#" + item 

        return encoded_data

    def decode(self, text: str) -> List[str]:
        result = []
        i = 0
        start_number = 0
        while i < len(text):
            character = text[i]
            if character == "#":
                length = int(text[start_number:i])
                start_to_read = i + 1
                result.append(text[start_to_read:start_to_read + length])
                i = start_to_read + length
                start_number = i
            else:
                i += 1
            
        return result