class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(s + 'é' for s in strs)

    def decode(self, s: str) -> List[str]:
        return s.split('é')[:-1]
