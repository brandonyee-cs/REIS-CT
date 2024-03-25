import random; import pandas as pd; import properties as prop

class systems:
    def __init__(self):
        self.userType_array = ['WC', 'MC', 'UC']; self.userType = random.choice(self.userType_array) #WC = Working Class | MC = Middle Class | UC = Upper Class
        
    def getuserType(self):
        return self.userType
    
    def balStart(self):
        if self.userType == 'WC': self.balance = 50000
        elif self.userType == 'MC': self.balance = 500000
        elif self.userType == 'UC': self.balance = 5000000
    
    def getProplist(self):
        df = self.df
        if self.userType == 'WC': self.df = pd.DataFrame(data=prop.wc_proplist); self.dictvar = prop.wc_proplist
        elif self.userType == 'MC': self.df = pd.DataFrame(data=prop.mc_proplist); self.dictvar = prop.mc_proplist
        elif self.userType == 'UC': self.df = pd.DataFrame(data=prop.uc_proplist); self.dictvar = prop.uc_proplist
        return self.df
    
    def morgage(self):
        #Mortgages a property
        propVal = self.prop[3]
        if self.balance >= propVal: self.balance -= propVal
        elif self.balance >= propVal: self.balance -= 0.06 * propVal
        else: self.propInfo == 'ERROR // PROPERTIES DISPLAYED INVALID \nReload to Reset'

    def buyProp(self):
        validpropID = False
        df = self.df
        while validpropID == False: 
            propID = int(input("Enter the ID (First Row) of the property you want to purchase: "))
            self.prop = self.df.get(propID)
            if self.prop is not None: break
            else: print("Invalid PropID; Try Again")
        self.prop = df.get(propID)

class timeline(systems):
    def __init__(self, userType, prop) -> None:
        systems.__init__(self,userType)

    def changeRate(self):
        pass