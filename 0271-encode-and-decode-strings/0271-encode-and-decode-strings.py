class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans=""
        for s in strs:
            x=str(len(s))
            ans+='/'+x+"#"+s
        return ans
         
    
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                # Step 1: Collect digits before '#'
                j = i - 1
                digits = ''
                while j >= 0 and s[j].isdigit() and s[j]!='/':
                    digits = s[j] + digits
                    j -= 1
                x = int(digits)
                # Step 2: Extract the word
                start = i + 1
                end = start + x
                ans.append(s[start:end])
                # Step 3: Move index to the end of the word
                i = end
            else:
                i += 1
        return ans


        
# # Create a Codec object
# codec = Codec()

# # Call the method and print result
# print(codec.encode(["Hello", "World"]))

# #Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))