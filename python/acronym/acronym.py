import re
def abbreviate(words):
    string=""

    for i in range(0,len(words.replace("_"," ").replace("-"," ").split())):
    
        string+=words.replace("_"," ").replace("-"," ").split()[i][0].upper()
        print(string)
    
        # #string+=i[0].upper()
        # if i[0]=='-':
        #     continue
        # if(i[0]=='_'):
        #     string+=i[1].upper()
        # else:
        #     string+=i[0].upper()
        # print(string)
    return string

abbreviate("The Road _Not_ Taken - vjh-K")