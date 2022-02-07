para = []
i = 1
y = 1
while True:
    print("Student", i, ":", end="")
    line = input()
    i += 1
    if line:
        para.append(line)
    else:
        break
list = len(para)
print("List word count :", list)
while True:
    if y <= list:
        for x in para:
            print(y,x)
            y += 1











