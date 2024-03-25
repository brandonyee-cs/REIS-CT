from systems import systems as sys
from systems import timeline as tl

print("Welcome to the Python DEMO for REIS-CT \nThis is DEMO was created as a submission for the CT LT Govs Computing Challenge.\nCreated by Brandon Yee, Rohak Gulia, and Shayaan Siddiqui.")

#Initialization
DEMO = sys()
sys.balStart(DEMO)

#Prints Basic Information
print(f"Player Type: {sys.getuserType(DEMO)} \nUC = Upper Class; MC = Middle Class; WC = Working Class")
print(f"Balance: {sys.getBalance(DEMO)}")

print(sys.getProplist(DEMO))
sys.buyProp(DEMO)
sys.morgage(DEMO)
print(sys.getBalance)
