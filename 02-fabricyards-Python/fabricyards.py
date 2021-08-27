# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricexcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards).
# Hint: you may want to use fabricyards, which you just wrote!


def fabricyards(inches):
 
    if inches%36 == 0:
        return inches//36
    else:
        yards = inches//36
        yards+=1
    return yards
 
def fabricexcess(inches):
 
    if inches%36 == 0:
        return inches%36
    else:
        yards = inches//36
        yards+=1
        fabric = ((yards*36)-inches) 
    return fabric