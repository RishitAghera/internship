

def decode(cipher):
    translate = dict(zip("zyxwvutsrqponmlkjihgfedcba0123456789", "abcdefghijklmnopqrstuvwxyz0123456789"))
    return "".join(translate[l] for l in cipher.lower() if l in translate)
    

def encode(ciphered_text):
    translate = dict(zip("zyxwvutsrqponmlkjihgfedcba0123456789", "abcdefghijklmnopqrstuvwxyz0123456789"))
    return  "".join([translate[i]  if i in translate else i for i in ciphered_text.lower()])



# print(encode("ab c"))