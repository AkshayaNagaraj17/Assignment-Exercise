c1={'s1':83,'s2':64,'s3':49,'s4':73}

above_70={}

for student , mark in c1.items():
    if mark>70:
        above_70[student]=mark
print(above_70)