import random
import properties as prop

class systems:
    def __init__(self):
        self.userType_array = ['WC', 'MC', 'UC'] #WC = Working Class | MC = Middle Class | UC = Upper Class
        self.userType = random.choice(self.userType_array)  # WC, MC or UC
        
    def getuserType(self):
        return self.userType
    
    def balStart(self):
        if self.userType == 'WC':
            self.balance = 'tempVal' #Working Class Starting Balance
        elif self.userType == 'MC':
            self.balance = 'tempVal' #Middle Class Starting Balance
        elif self.userType == 'UC':
            self.balance = 'tempVal' #Upper Class Starting Balance
    
    def getBalance(self):
        return self.balance #Returns Balance | Visuals tbd
    
    def propDisplay(self):
        if self.userType == 'WC':
            pass #Create Pandas Data Frame
        elif self.userType == 'MC':
            pass #Create Pandas Data Frame
        elif self.userType == 'UC':
            pass #Create Pandas Data Frame
    
    def morgage(self, propID, propVal, bT):
        '''Mortgages a property'''
        if bT == True and self.getBalance >= propVal:
            self.balance -= propVal
            self.propInfo = [propID, True , False] #propID, Purchased?, Have to Pay Rent?
            return self.propInfo
        elif bT == False and self.getBalance >= propVal:
            self.balance -= 0.06 * propVal
            self.propInfo = [propID, True, True] #propID, Purchased?, Have to Pay Rent?
            return self.propInfo
        else:
            self.propInfo == 'ERROR // PROPERTIES DISPLAYED INVALID \nReload to Reset'
            return self.propInfo

class timeline(systems):
    def __init__(self, userType, propInfo) -> None:
        systems.__init__(self,userType,propInfo)

    def changeRate(self):
        tempVar 