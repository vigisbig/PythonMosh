weight = input("What's your weight? ")
units = input("(k)gs or (l)bs? ")

if units == ("k" or "K"):

    wpd = float(weight)/0.45

    print("Your weight is " +str(wpd) +"pounds")

elif units == ("l" or "L"):

    wkg = float(weight)*0.45

    print("Your weight is " +str(wkg) +"kgs")