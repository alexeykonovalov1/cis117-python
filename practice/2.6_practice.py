# This is my fifth Python programming practice file.
# Author: Alexey Konovalov
# Date: 28.08.2026


import math

sin = math.sin(math.pi / 6)
cos = math.cos(math.pi / 6)
tan = sin / cos

print(sin)
print(cos)
print(tan)

print()

rounded_sin = round(sin, 2) 
rounded_cos = round(cos, 2)
rounded_tan = round(tan, 2)

print("Sin(π / 6) = " + str(rounded_sin) + " (2 d.p.)")
print("Cos(π / 6) = " + str(rounded_cos) + " (2 d.p.)")
print("Tan(π / 6) = " + str(rounded_tan) + " (2 d.p.)")