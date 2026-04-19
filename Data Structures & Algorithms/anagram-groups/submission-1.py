class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        result = []

        if strs == "":
            return []

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in dict:
                dict[sorted_word] = []
            
            dict[sorted_word].append(word)
        
        for val in dict.values():
            result.append(val)
        
        return result