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

print(toBin(message))

print(pad512M(toBin(message)))
