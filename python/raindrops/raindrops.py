def convert(number):
    result=""
    if number%3== 0:
        result+="Pling"
    if number % 5==0:
        result+="Plang"
    if number % 7 == 0:
        result+="Plong"
    if result == "":
    # if number % 7 != 0 and number % 3 != 0 and number % 5 != 0:
        result=str(number)    
    return result