weight = float(input("What is your weight? "))
unit = input("(K)g or (L)b? ")

if unit.upper() == "K":

  WP = weight/0.45
  
  print("Weight in pound is "+ str(WP)+"Pound")

  
else:

  WK = weight*0.45
  
  print("Weight in kg is "+ str(WK)+"Kilogram")
