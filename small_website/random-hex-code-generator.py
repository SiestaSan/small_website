import random as rd

hex_code = []
hex_code.append("#")
for i in range (6):
    hex_code.append(rd.choice("0123456789ABCDEF"))
print(f"Here is the random hex code: {''.join(hex_code)}")