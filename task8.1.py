def is_sorted (x):
    z=True
    for i in range (len(x)-1):
        if x[i]>x[i+1]:
            z=False
            return(z)
        else:
            continue
    return z
x=[]
print("Enter list numbers(space to break)")
while True:
    n=input()
    if n==" ":
        break
    else:
        x.append(int(n)) 
print(is_sorted(x))