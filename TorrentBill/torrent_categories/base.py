class Base():
    def __init__(self):
        self.intoRupees=0.01

    def inputUnit(self):
        self.unit=int(input('Enter Unit:'))

    def inputPhase(self):
        """ Phase input (1 or 3)"""
        subcat=("[1] Single Phase",
                "[2] Three Phase",
                "[0] Exit")

        print(*subcat,sep="\n") 
        print("==============================================="*2)
        
        self.phase=int(input("Enter Phase:"))

        if self.phase>=len(subcat) or self.phase<=0:
            print("Wrong Input..Please try again")
            return
        return self.phase
        
    def amount_calculation(self,conditions):
        self.amt=0
             
        for i,j in conditions.items():
            if self.unit>i and self.unit>0:
                self.amt+=j*i;
                self.unit-=i
            else:
                self.amt+=self.unit*j
                break
                
        return self.amt
            