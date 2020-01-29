from .base import Base
class NonRpg(Base)
    def __init__(self,conditions):
        self.inputUnit()
        self.conditions=conditions
        self.fixrate=450

        self.tot_amt=self.amount_calculation(self.conditions)+self.unit*self.fixrate
        self.tot_amt=self.tot_amt*self.intoRupees
    # if self.unit<=15 and self.unit>5:
    #     amt+=
    
