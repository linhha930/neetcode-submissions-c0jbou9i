class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_arr = []
        result = ""

        for string in strs:
            str_len = len(string)
            encode_arr.append(str(str_len))
            encode_arr.append("#")
            encode_arr.append(string)
        
        result = ''.join(encode_arr)
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        # use pointers to "skip" ahead
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1:j + 1 + length]
            result.append(word)

            # skip first word/phrase that's been parsed
            i = j + 1 + length
            
        return result

        

