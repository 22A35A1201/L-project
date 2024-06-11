def check(n):
    if n%2==0:
        print("yes")
    elif (n+1)%2==0:
        print("no")
    else:
        print("enter again")

b=[2,3,471,7,13]
a=map(check,b)
print(list(a))