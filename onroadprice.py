actual_price = int(input("enter actual price"))


if actual_price >72000 and actual_price < 150000:
    income_tax=actual_price*10/100
    insurance=actual_price*15/100
    onroadprice=actual_price+income_tax+insurance
    print(onroadprice)

elif actual_price>150000 and actual_price<200000:
    income_tax=actual_price*25/100
    insurance=actual_price*20/100
    onroadprice=actual_price+income_tax+insurance
    print(onroadprice)

elif actual_price>2000:
    income_tax=actual_price*35/100
    insurance=actual_price*28/100
    onroadprice=actual_price+income_tax+insurance
    print(onroadprice)
else:
    ("entar valid value")



