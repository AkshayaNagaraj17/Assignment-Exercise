import math
dict={'x':2,'y':3,'z':4}
sq={}

for var,num in dict.items():
    n=pow(num,2)
    sq[var]=n
print(sq)
