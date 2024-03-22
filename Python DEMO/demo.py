from systems import systems as sys
from systems import timeline as tl

print("Welcome to the Python DEMO for REIS-CT \nThis is DEMO was created as a submission for the CT LT Govs Computing Challenge.\nCreated by Brandon Yee, Rohak Gulia, and Shayaan Siddiqui.")

#Setting Up Through Systems Start Functions

DEMO = sys()
demo_usertype = sys.getuserType(DEMO)
sys.balStart(DEMO)
demo_balance = sys.getBalance(DEMO)

print(f"Player Type: {demo_usertype} \nUC = Upper Class; MC = Middle Class; WC = Working Class")
print(f"Balance: {demo_balance}")

print(sys.getProplist(DEMO))
sys.getProp(DEMO)

