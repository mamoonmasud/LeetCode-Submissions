class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(f"{len(ss)}|{ss}"for ss in strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        i = 0
        print(s)
        while i <len(s):
            x1 = s.find("|", i)
            
            i = x1 + 1 + int(s[i:x1])
            ans.append(s[x1+1:i])
            
        return ans
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))