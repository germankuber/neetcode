class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        if len(s) != len(t):
            return False
        
        def get_dict(word:str)-> dict:
            dict_to_return = {}
            for letter in word:
                if letter in dict_to_return:
                    dict_to_return[letter] += 1
                else:
                    dict_to_return[letter] = 1
            return dict_to_return
        
        return get_dict(s) == get_dict(t)