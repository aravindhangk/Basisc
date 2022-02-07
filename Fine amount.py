day = int(input("Enter the number of the delayed day :"))
if day <=4:
    print("there is no fine")
elif day >=5 and day <=10:
    fine1 = day*2
    print(fine1)
elif day >=11 and day <=20:
    fine2 = day*3
    print(fine2)
else:
    fine3 = day*4
    print(fine3)


