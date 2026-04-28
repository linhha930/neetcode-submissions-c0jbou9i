class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []

        for ch in s:
            if ch.isalnum():
                filtered.append(ch.lower())

        l, r = 0, len(filtered) - 1

        while l < r:
            if filtered[l] != filtered[r]:
                return False
            l += 1
            r -= 1

        return True