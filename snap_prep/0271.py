class Codec:

    def encode(self, strs):
        encoded = ''
        for s in strs:
            encoded += s + '**,**'
        encoded = encoded[0:len(encoded)-5]
        return encoded
        

    def decode(self, s):
        decoded = s.split('**,**')
        if decoded[0] is "":
            return []
        else:
            return decoded
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
