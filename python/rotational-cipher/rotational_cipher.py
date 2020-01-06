import re
def rotate(text, key):
    string=""
    for i in text:
        if((65<=ord(i) and ord(i)<=90) or (97<=ord(i) and ord(i)<=122)):
            if(i.isupper()):
                if((ord(i)+key)>90):
                    string+=chr(((ord(i)+key)-91)+65)
                else:
                    string+=(chr(ord(i)+key))
            else:
                if((ord(i)+key)>122):
                    string+=chr(((ord(i)+key)-123)+97)
                else:
                    string+=(chr(ord(i)+key))
        else:
            if(re.match("[^\w']| '|' |'[^\w]|_|'$",i)==False):
                string+=" "
            else:
                string+=i
    return string


#print(rotate("Th'e quick! brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire gur ynml qbt",13))