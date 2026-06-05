n=input("Enter the string: ")
ls=n.lstrip()
print(ls)
sign=1
num=""
if ls[0]=="-":
    sign=-1
    ls=ls[1:]
elif ls[0]=="+":
    ls=ls[1:]
for i in ls:
    if i.isdigit():
        num+=i
    else:
        break
result=int(num)*sign