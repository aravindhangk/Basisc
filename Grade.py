
m1, m2, m3 = list(map(int, input("Enter M1 M2 M3 mark:").split()))
total = int(m1+m2+m3)
average = int(total/3)
print("Total :", total)
print("Average :", average)
if m1 >=35 and m2 >=35 and m3 >=35:
    print("Pass")
    if average >=80:
        Print("Grade:A")
    elif average <=79 and average >=60:
        print("Grade:B")
    elif average <=59 and average >= 50:
        print("Grade: C")
    else:
        print("Grade: D")
else:
    print("Result : Fail")
    print("No Grade")





