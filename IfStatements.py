temperature = 9                    # We use IF statements to make decisions

if temperature > 30:                # If followed by condition to evaluate. Following line is automatically indented
    print("It's a hot day")         # to indicate the block of code, no curly braces
    print("Drink lots of water")    # Use of apostrophe is avoided and use " " so that Python does not get confused

elif temperature > 20:              # elif is a short form for elseif, there's no elseif in Python
    print("It's a nice day")

elif temperature > 10:
    print("It's a bit cold")

else:                               # will be executed if none of the above conditions are true
    print("It's cold")

print("Done")                       # Note that there's no indent, so it's not part of IF block and will be executed
                                    # regardless of the IF condition being ture or false.


