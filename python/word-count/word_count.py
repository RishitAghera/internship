import re
def count_words(sentence):
    string = ""
    # string =re.sub("'$","",(re.sub("[^a-zA-z0-9 ']| '|' "," ",sentence))).split()
    string =re.sub("[^\w ']| '|' |'[^\w]|_|'$"," ",sentence).lower().strip().split()

    
    print(string)
   # string =re.sub("'!","",string)
    ans={}
    for i in string:
        ans[i]=string.count(i)
        
    
    return ans


print(count_words("one,\ntwo,\n'three'"))