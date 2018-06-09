#convert_to_meters.py

conversion_dict = {"feet": 0.3048, "miles": 1609.34, "kilometers": 1000}

units = input("What type of unit do you want to convert? ")
while units not in conversion_dict:
    units = input("What type of unit do you want to convert? ")
distance = int(input("How many? "))
print (str(distance), str(units), "equals", str((conversion_dict[units] * distance)), "meters.")
