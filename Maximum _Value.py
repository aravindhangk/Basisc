para =[]
m1 = int(input("Enter M1 Mark :"))
m2 = int(input("Enter M2 Mark :"))
m3 = int(input("Enter M3 Mark :"))
para.append(m1)
para.append(m2)
para.append(m3)
a = para.index(max(para))
b= para.index(min(para))
if a == 0:
    print("M1 is Maximum mark : ",max(para))
if a == 1:
    print("M2 is Maximum mark : ",max(para))
if a == 2:
    print("M3 is Maximum mark : ",max(para))