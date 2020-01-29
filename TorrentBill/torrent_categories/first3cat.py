from .base import Base
class First3cat(Base):
    def __init__(self,phase,conditions,chargephase1,chargephase3):
        super().__init__()
        self.inputUnit()
        self.phase=0
        self.phase1=chargephase1 #charge of phase 1
        self.phase3=chargephase3 #cahrge of phase 2
        if phase==True:
            # self.phase1=25
            # self.phase3=65
            self.phase=self.inputPhase()
            if self.phase==1:
                self.phase=self.phase1
            else:
                self.phase=self.phase3     
            
        self.conditions=conditions
        # print(type(self.amount_calculation(self.conditions))type(self.phase))
        self.tot_amt=int(self.amount_calculation(self.conditions))+int(self.phase)
        self.tot_amt=self.tot_amt*self.intoRupees
        