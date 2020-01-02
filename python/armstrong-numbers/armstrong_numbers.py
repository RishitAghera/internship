import math
def is_armstrong_number(number):
    sum=0
    leng=len(str(number))
    # print(type(leng))
    
    for i in str(number):
        sum+=math.pow(int(i),leng)
    if(sum == number):
        return True
    else:
        return False
    
print(is_armstrong_number(123))