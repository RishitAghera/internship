def is_isogram(string):
    str1=[]
#    print(string.lower().replace(" ","").replace("-",""))
    for x in (string.lower().replace(" ","").replace("-","")):
        if(x in str1):
            return False
        else:
            str1.append(x)
    return True

#is_isogram("six-year-old")