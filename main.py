#defining Initial hashes
H0 = 0x6a09e667
H1 = 0xbb67ae85
H2 = 0x3c6ef372
H3 = 0xa54ff53a
H4 = 0x510e527f
H5 = 0x9b05688c
H6 = 0x1f83d9ab
H7 = 0x5be0cd19


def readRoundConsts():
    with open("roundConstants.txt", 'r') as f:
        K=f.readlines()
    for i in K:
        i=i.rstrip()
    return K


def toBin(message):
    return "".join([bin(y)[2:].zfill(8) for y in [ord(x) for x in message]])
    
def pad512M(binMsg):
    sizePadding=bin(len(message))[2:].zfill(64)
    binMsg+='1'
    while (len(binMsg)%512!=448 or len(binMsg)<64):
        binMsg+='0'
    binMsg+=sizePadding
    return binMsg
    
message = "STOP"

paddedMsg = pad512M(toBin(message))



def rightRotate(word, c):
    c=c%len(word)
    return word[-c:] + word[:-c]

def chunkLoop(w):
    for i in range(16,64):
        s0=rightRotate(w[i-15], 7) ^ rightRotate(w[i-15], 18) ^ (w[i-15]>>3)
        print(s0)

def createChunk(paddedMsg):
    chunks = [paddedMsg[i:i+512] for i in range(len(paddedMsg)//512)]
    for chunk in chunks:
        chunk += "0"*1536
        words = [chunk[i:i+32] for i in range(len(chunk)//32)]
        chunkLoop(words)
        

createChunk(paddedMsg)












