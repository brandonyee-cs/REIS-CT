from systems import systems as sys
from systems import timeline as tl

print("Welcome to the Python DEMO for REIS-CT \nThis is DEMO was created as a submission for the CT LT Govs Computing Challenge.\nCreated by Brandon Yee, Rohak Gulia, and Shayaan Siddiqui.")

#Setting Up Through Systems Start Functions

sys()
demo_usertype = sys.getuserType()
sys.balStart()
demo_balance = sys.getBalance()

print(f"Player Type: {demo_usertype} \nUC = Upper Class; MC = Middle Class; WC = Working Class")
print(f"Balance: {demo_balance}")

sys.propDisplay()