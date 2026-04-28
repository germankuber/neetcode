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
                to_read =  text[start_number:i]
                start_to_read = i + 1
                text_to_read = text[start_to_read:start_to_read + int(to_read)]
                result.append(text_to_read)
                i = start_to_read + int(to_read)
                start_number = i
            else:
                i += 1
            
        return result