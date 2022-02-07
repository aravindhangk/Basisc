data = {
    "x":{
    "name":"1",
    "age":"2",
    "language":"3"
 }
}


A = input("set your roll number:")
data[A] = data["x"]
Name =input("enter your name :")
Age = input("enter your age :")
Language = input("enter your language :")


data["x"]["name"] = Name
data["x"]["age"] = Age
data["x"]["language"] = Language
"""for x in data:
    print(x,"------->",data[x]) """
a =input("Enter your name for result :")
def fun(a):
    return data[a]
for x in fun(a):
    print(x)

