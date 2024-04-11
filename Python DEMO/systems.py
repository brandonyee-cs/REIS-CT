import random; import time as t; import pandas as pd; import properties as prop; import timeline as tln

class systems:
    def __init__(self):
        self.userType_array = ['WC', 'MC', 'UC']; self.userType = random.choice(self.userType_array) #WC = Working Class | MC = Middle Class | UC = Upper Class
    
    def balStart(self):
        if self.userType == 'WC': self.balance = 50000
        elif self.userType == 'MC': self.balance = 500000
        elif self.userType == 'UC': self.balance = 5000000
    
    def getProplist(self):
        if self.userType == 'WC': self.df = pd.DataFrame(data=prop.wc_proplist); self.dictvar = prop.wc_proplist; return self.df
        elif self.userType == 'MC': self.df = pd.DataFrame(data=prop.mc_proplist); self.dictvar = prop.mc_proplist; return self.df
        elif self.userType == 'UC': self.df = pd.DataFrame(data=prop.uc_proplist); self.dictvar = prop.uc_proplist; return self.df
    
    def morgage(self):
        propVal = self.prop[3]
        if self.balance >= propVal: self.balance -= propVal
        elif self.balance >= propVal: self.balance -= 0.06 * propVal
        else: print('ERROR // PROPERTIES DISPLAYED INVALID \nReload to Reset')

    def buyProp(self):
        validpropID = False
        while validpropID == False: 
            propID = int(input("Enter the ID (First Row) of the property you want to purchase: ")); self.prop = self.df.get(propID)
            if self.prop is not None: break
            else: print("Invalid PropID; Try Again")
        self.prop = (self.df).get(propID)

class timeline(systems):
    def __init__(self, userType, prop) -> None:
        systems.__init__(self,userType)

    def changeRate(self):
        if self.prop[0] == 'NYC': self.tl = tln.nyc_events
        elif self.prop[0] == 'Miami': self.tl = tln.miama_events
        elif self.prop[0] == 'Weston': self.tl = tln.weston_events
        elif self.prop[0] == 'Great Neck': self.tl = tln.greatneck_events
        elif self.prop[0] == 'Atlanta': self.tl = tln.atlanta_events
        elif self.prop[0] == 'LA': self.tl = tln.la_events
        for i in range(len(self.tl)): print(f"Due to: {self.prop[i][2]}, your property dropped {self.prop[i][1]}%."); t.sleep(0.5)
        finalvalue = 3*self.prop[2] + self.prop[3] * (self.tl[-1][0]/100); print(f"Final value of your property after 1 year: {finalvalue}")