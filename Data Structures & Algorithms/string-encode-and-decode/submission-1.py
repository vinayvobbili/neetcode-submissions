class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(s + 'é' for s in strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        decoded_strs = []
        decoded_str = ''
        for c in s:
            # print(c)
            # print(decoded_str)
            if c == 'é':
                decoded_strs.append(decoded_str)
                # print(decoded_str)
                decoded_str = ''
            else:
                decoded_str = decoded_str + c
        # print(decoded_strs)
        return decoded_strs
