weight = int(input("What is your weight? "))
unit = input("(K)g or (L)b?" )

if unit.upper == "K":

  WP = float(weight)/0.45
  
  print("Weight in pound is "+ str(WP)"Pound")

  
else:

  WK = float(weight)*0.45
  
  print("Weight in kg is "+ str(WK)"Kilogram")
