def is_pangram(sentence):
    check=True
    sentence=sentence.lower()
    for i in range(97,123):
        if chr(i) not in sentence:
            return False
            
    # for i in range(48,58):
    #     if chr(i) in sentence:
    #         return False 

    return check    

#print(is_pangram("Quick brown fox jumps over the little lazy dog"))
