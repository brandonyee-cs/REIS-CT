import random
import pandas as pd
import properties as prop

class systems:
    def __init__(self):
        self.userType_array = ['WC', 'MC', 'UC'] #WC = Working Class | MC = Middle Class | UC = Upper Class
        self.userType = random.choice(self.userType_array)  # WC, MC or UC
        
    def getuserType(self):
        return self.userType
    
    def balStart(self):
        if self.userType == 'WC':
            self.balance = 50000 #Working Class Starting Balance
        elif self.userType == 'MC':
            self.balance = 500000 #Middle Class Starting Balance
        elif self.userType == 'UC':
            self.balance = 5000000 #Upper Class Starting Balance
    
    def getBalance(self):
        return self.balance #Returns Balance | Visuals tbd
    
    def getProplist(self):
        if self.userType == 'WC':
            self.df = pd.DataFrame(data=prop.wc_proplist)
            self.dictvar = prop.wc_proplist
        elif self.userType == 'MC':
            self.df = pd.DataFrame(data=prop.mc_proplist)
            self.dictvar = prop.mc_proplist
        elif self.userType == 'UC':
            self.df = pd.DataFrame(data=prop.uc_proplist)
            self.dictvar = prop.uc_proplist
        #df.index = ['Location:', 'Bed/Bath:', 'Est.Cost:', 'Morgage Cost:'] Fix Row Names
        return self.df
    
    def getProp(self):
            validpropID = False
            while validpropID != True:
                propID = input("Enter the ID (First Row) of the property you want to purchase: ")
                if propID in self.dictvar:
                    validpropID = True
                else:
                    print("Invalid PropID; Try Again")
            self.prop = self.df.get(propID)
            return self.prop
            
                

    def morgage(self):
        #Mortgages a property
        propVal = self.prop[3]
        if self.getBalance >= propVal:
            self.balance -= propVal
            return self.propInfo
        elif self.getBalance >= propVal:
            self.balance -= 0.06 * propVal
        else:
            self.propInfo == 'ERROR // PROPERTIES DISPLAYED INVALID \nReload to Reset'
            return self.propInfo

class timeline(systems):
    def __init__(self, userType, prop) -> None:
        systems.__init__(self,userType)

    def changeRate(self):
        pass