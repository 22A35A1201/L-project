a = int(input("enter a integer"))

if a%3==0 and a%6==0:
    print("good number")
elif a%2==0 and a%7==0:
    print("average number")
elif a%4==0 or a%9==0:
    print("awesome number")
else:
    print("bad number")