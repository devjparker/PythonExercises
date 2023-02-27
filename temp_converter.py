"""This function is a temperature converter.
The goal is to have the user input the number,
input the current unit (F or C), and then
output the other unit."""

def temp_converter(num, unit) :
    if unit.lower() == "c" :
        return num*1.8 + 32
        
    else :
        return (num-32)*.5556
    

print(temp_converter(1, "F"))
print(temp_converter(32, "C"))
print(temp_converter(-100, "c"))
print(temp_converter(100, "f"))
