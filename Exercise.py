my_list=['cat','frog','elephant','crow']
length=[]
for i in my_list:
    len1=len(i)
    length.append(len1)
print(f"Keys:{my_list}")
print(f"Length: {length}")

merging=dict(zip(my_list,length))
print(merging)