def temp_convert(temp,unit):
    if unit.upper() == "C":
        return temp * 9/5 + 32
    elif unit.upper() == "F": 
        return (temp-32) * 5/9
    else:
        print("Please provide the valid unit...")
temp = int(input("Enter the temperature: "))
unit = input("Enter the unit of temperature (C/F): ")
print(temp_convert(temp,unit))