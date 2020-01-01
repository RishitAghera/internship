def score(word):
    s1=["A", "E", "I", "O","U", "L", "N", "R","S", "T"]
    s2=["D","G"]
    s3=["B","C","M","P"]
    s4=["F","H","V","W","Y"]
    s5=["J","X"]
    s6=["Q","Z"]
    cnt=0
    for i in word.upper():
        if(i in s1):
            cnt+=1 
        elif(i in s2):
            cnt+=2
        elif(i in s3):
            cnt+=3
        elif(i in s4):
            cnt+=4
        elif(i in s5):
            cnt+=8
        elif(i in s6):
            cnt+=10
        else:
            cnt+=5    
    return cnt

# print(score("abc"))