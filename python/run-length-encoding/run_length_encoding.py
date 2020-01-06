import re

def decode(string):
    temp={}
    a,b=[],[]
    tmp=""
    for i in string:
        if(i.isnumeric()==True):
            tmp+=str(i)
        else:
            #w.append(i)
            if(tmp==""):
                tmp+="1"
            #n.append(int(tmp))
            #temp[w[a]]=n[a]
            a.append(i)
            b.append(int(tmp))
            temp[i]=int(tmp)        
            tmp=""                
            
    ans=""
    for p,q in zip(a,b):
        ans+=p*q

    return ans

def encode(string):
    if(len(string)==0):
        return ""
    temp=string[0]
    count=0
    ans=""
    for i in string:
        if(i!=temp):
            ans+=str(count)+temp if count>1 else temp
            temp=i
            count=1
        else:
            count+=1

    ans+=str(count)+temp if count>1 else temp
    return ans

# print(decode("3z 2Z2 2p3 m"))
print(encode(""))
