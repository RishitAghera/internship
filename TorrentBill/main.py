import torrent_categories
from collections import OrderedDict

if __name__=='__main__':                                            #Function name         ,'phase',                 conditions       charge: phase1 , phase3  
    category={1:("[1] RGP : Residential General Purpose",   torrent_categories.First3cat,    True,   OrderedDict({50:320,150:390,999999:490}),  25   , 65),
        2:("[2] BPL : Below Poverty Line",torrent_categories.First3cat,'',OrderedDict({30:150,20:320,150:390,99999:490}),'',''),
        3:("[3] GLP : General Lighting Purpose",torrent_categories.First3cat,True,OrderedDict({200:410,99999:480}),30,70),
        4:("[4] Non-RGP : Low Tension Service for Commercial and Industrial Purpose",torrent_categories.First3cat,'',OrderedDict({5:70,15:90}),70,90),
        5:("[5] SL : Low Tension Tension Street Light Service",torrent_categories.Sl,'','','',''),
        # 5:("[5] LTP (AG) : Agriculture Service",torrent_categories.LTP_AG),
        # 7:("[7] LEV : LT- Electric Vehicle Charging Stations",torrent_categories.LevLt),
        # 8:("[8] TMP : Low Tension Temporary Supply",torrent_categories.TMP),
        0:("[0] Exit","")}
    
    choice=0

    print("==============================================="*3,)
    print(*map(lambda p:p[0],category.values()),sep="\n") #Print on console option of the Bill Type
    print("==============================================="*3,)
    
    choice=int(input("Enter Bill Type Index Number:"))
    # try:
    if choice<0 or choice>=len(category):
        print(f"Input in between 0 to {len(category)-1}")
    else:
        if choice==0:
            exit()
        print(category[choice][1](category[choice][2],category[choice][3],category[choice][4],category[choice][5]).tot_amt)#function(phase,conditions)

    # except Exception as e:
    #     print("Enter Only The Integer Field")
        #print(e)