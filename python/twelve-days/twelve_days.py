# def recite(start_verse, end_verse):
    
#     #lst1={1:,2:,3:,4:,5:,6:,7:,8:,9:,10:,11:,12:}

#     lst2={12:"twelve Drummers Drumming, ",
#             11:"eleven Pipers Piping, ",
#             10:"ten Lords-a-Leaping, ",
#             9:"nine Ladies Dancing, ",
#             8:"eight Maids-a-Milking, ",
#             7:"seven Swans-a-Swimming, ",
#             6:"six Geese-a-Laying, ",
#             5:"five Gold Rings, ",
#             4:"four Calling Birds, ",
#             3:"three French Hens, ",
#             2:"two Turtle Doves, ",
#             1:"and Partridge in a Pear Tree.",
#             0:" a Partridge in a Pear Tree."}

#     finlist=[]
    
#     temp=first(start_verse)

#     for i in range(end_verse,0,-1):
#         temp+=lst2[i]
            
#     return [temp]



# def first(num):

#     if(num==1):
#         text="one"
#     elif(num==2):
#         text="second"
#     elif(num==3):
#         text="third"
#     elif(num==4):
#         text="fourth"
#     elif(num==5):
#         text="fifth"
#     elif(num==6):
#         text="sixth"
#     elif(num==7):
#         text="seventh"
#     elif(num==8):
#         text="eighth"
#     elif(num==9):
#         text="ninth"
#     elif(num==10):
#         text="tenth"
#     elif(num==11):
#         text="eleventh"
#     elif(num==12):
#         text="twelfth"
        

#     string="On the "+text+" day of Christmas my true love gave to me: "
#     return string
    
# print(recite(4,4))

def verse(n):
    surprise=''.join([
        "and a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
    ][n::-1])
    if n==0:
        surprise=surprise.replace('and ',"")
    return surprise

def recite(start_verse, end_verse):
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth"]
    return ["On the "+day[n-1]+" day of Christmas my true love gave to me: "+verse(n-1) for n in range(start_verse,end_verse+1)]
    