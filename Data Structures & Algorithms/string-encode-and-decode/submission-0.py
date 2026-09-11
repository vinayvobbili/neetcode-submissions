class Solution:

    def encode(self, strs: List[str]) -> str:
        print(strs)
        encoded_string = ''
        for s in strs:
            encoded_string = encoded_string + s + 'é'
        # print(encoded_string)
        return encoded_string

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
