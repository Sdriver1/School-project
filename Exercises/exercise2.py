# Weight converter

weight = input("Weight: ")
unit = input ("Is that weight in (K)g or (L)bs: ")
if unit.upper() == "L":
    weightk = float(weight)/2.205
    print("Weight in Kg: " + str(int(weightk)) + " kg") # (lbs to kg]
elif unit.upper() == "K":
    weightl = float(weight)*2.205
    print("Weigth in Lbs: " + str(int(weightl))+ " lbs") # (kg to lbs]
    