def rgp(unit):
    phase=int(input("Enter Phase: 1 for single and 3 for three phase:"))

    while phase not in (1,3):
        phase=int(input("Please enter correct phase '1' or '3'."))
    
    amt=0.00
    if 0<=unit and unit<=50:
        amt+=unit*320
    elif 51<=unit and unit<=200:
        amt+=16000
        amt+=(unit-50)*390
    elif unit>200:
        amt+=74500
        amt+=(unit-200)*490

    else:
        return print('Please enter valid unit!!')
        
        
    return print('Your payable amount is:{} Rs.'.format((amt+2500)/100 if phase==1 else (amt+6500)/100))

def rgpBpl(unit):
    amt=0.00
    if 0<=unit and unit<=30:
        amt+=unit*150  
    elif 31<=unit and unit<=50:
        amt+=4500
        amt+=(unit-30)*320
    elif 51<=unit and unit<=200:
        amt+=4500+6400
        amt+=(unit-50)*390
    elif unit>200:
        amt+=74500
        amt+=(unit-200)*490
    else:
        return print('Please enter valid unit!!')
        
        
    return print('Your payable amount is:{} Rs.'.format((amt+500)/100))


def glp(unit):
    phase=int(input("Enter Phase: 1 for single and 3 for three phase:"))

    while phase not in (1,3):
        phase=int(input("Please enter correct phase '1' or '3'."))
    
    amt=0.00
    if 0<=unit and unit<=200:
        amt+=unit*410
    elif 200<unit:
        amt+=82000
        amt+=(unit-200)*480
    else:
        return print('Please enter valid unit!!')

    return print('Your payable amount is:{} Rs.'.format((amt+3000)/100 if phase==1 else (amt+7000)/100))


def nonRgp(unit):

    #taking 1 kW as 1 Unit

    amt=0.00
    if 0<=unit and unit<=5:
        amt+=unit*450 + unit*7000
    elif 5<unit and unit<=15:
        amt+=unit*450 + unit*9000
    elif unit>15:
        amt+=unit*450
    else:
        return print('Please enter valid unit!!')
        
    return print('Your payable amount is:{} Rs.'.format(amt/100))


def ltp(unit):
    #1kWh=1.34bhp-h
    amt=330*unit
    bamt=unit*1.34*1000


    if amt<bamt:
        return print('Your payable amount is:{} Rs.'.format(bamt/100))
    else:
        return print('Your payable amount is:{} Rs.'.format(amt/100))

def sl(unit):
    return print('Your payable amount is:{} Rs.'.format(unit*420/100))


def lev(unit):
    return print('Your payable amount is:{} Rs.'.format((unit*410/100)+25))



if __name__ == "__main__":
    cycle=0
    while cycle==0:
        print('---------Category----------')
        print('1.RGP : Residential General Purpose')
        print('2.RGP - BPL')
        print('3.GLP : General Lighting Purpose')
        print('4.Non-RGP : Low Tension Service for Commercial and Industrial Purpose')
        print('5.LTP (AG) : Agriculture Service')
        print('6.SL : Low Tension Tension Street Light Servic')
        print('7.LEV : LT- Electric Vehicle Charging Stations')
        print('----------------------------')
        choice=int(input("Enter Category:"))
        unit=int(input("Enter Unit:"))
        
        if choice==1:
            rgp(unit)
            cycle+=1
        elif choice==2:
            rgpBpl(unit)
            cycle+=1
        elif choice==3:
            glp(unit)
            cycle+=1
        elif choice==4:
            nonRgp(unit)
            cycle+=1
        elif choice==5:
            ltp(unit)
            cycle+=1
        elif choice==6:
            sl(unit)
            cycle+=1
        elif choice==7:
            lev(unit)
            cycle+=1
        else:
            print("--------XXXXXX---------")
            print("Choice is not valid!Enter again:")
            print("--------XXXXXX---------")