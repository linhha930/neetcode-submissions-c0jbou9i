class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        if len(s) != len(t):
            return False

        char_arr_s = list(s)
        char_arr_t = list(t)

        for letter in char_arr_s:
            if letter not in dict:
                dict[letter] = 1
            else: 
                dict[letter] += 1

        for letter in char_arr_t:
            if letter in dict:
                dict[letter] -= 1

        for value in dict.values():
            if value != 0:
                return False
        
        return True
         