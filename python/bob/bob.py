import re
def response(hey_bob):
    
    if(hey_bob.isupper() and hey_bob.rstrip().endswith("?")):
        return "Calm down, I know what I'm doing!"
        
    elif(hey_bob.isupper()):
        return "Whoa, chill out!"
    elif(hey_bob.rstrip().endswith("?")):
        return "Sure."
    elif(re.sub(r"[\n\r\t\s]","",hey_bob)==""):
        return "Fine. Be that way!"
    else:
        return "Whatever."
    

print(response("dv rwf"))