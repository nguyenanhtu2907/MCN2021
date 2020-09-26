class prefixcodetree:
    def __init__(self):
        super().__init__()
    codeword = {}
    def insert(self,code, symbol):
        key=''.join(str(x) for x in code)
        self.codeword[key]=symbol 
    def decode(self, encodedData, datalen):
        codes = self.codeword.keys()
        result = ''
        inp = encodedData.hex()
        mystr = bin(int(inp, 16))[2:]
        i=0
        while len(mystr[i:]) != (len(mystr)-datalen):
            for code in codes:
                if mystr[i:].startswith(code):
                    i+=len(code)
                    result+=self.codeword[code]
                    break
        return result

#test
codebook = {
    'x1':[0],
    'x2':[1,0,0],
    'x3':[1,0,1],
    'x4':[1,1]
}
tree = prefixcodetree()
for symbol in codebook:
    tree.insert(codebook[symbol],symbol)
print(tree.decode(b'\xd2\x9f\x20', 21))


