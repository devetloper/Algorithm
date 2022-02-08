line= "python is powerful that raaedtioeiwu"
line_without_aeiou=[i for i in line if i != "a" and i != "e" and i != "i" and i != "o" and i != "u"]
print("".join(line_without_aeiou))

