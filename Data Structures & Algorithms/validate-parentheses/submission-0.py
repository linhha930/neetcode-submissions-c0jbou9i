class Solution:
    def isValid(self, s: str) -> bool:
        # map closing brackets to opening (faster to check keys)
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        if not s:
            return True

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            else:
                # if closing bracket, check if it matches most recent open bracket
                if not stack:
                    return False
                
                # last open bracket
                last_char = stack.pop()
                if last_char != bracket_map[char]: # compare last open to dict values
                    return False
        
        if stack:
            return False
        else:
            return True
                    
        