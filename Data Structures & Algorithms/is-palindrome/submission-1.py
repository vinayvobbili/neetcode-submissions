class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        n = len(cleaned)
        for i in range(n//2):
            if cleaned[i] == cleaned[n-i-1]:
                continue
            else:
                return False
        return True