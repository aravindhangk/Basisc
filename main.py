print(10+100)
Variable = "   Value   "
print(Variable)
print(int(10.0))
print(float(1))
Number1 = 10
Number1 += 10
Number2 = Number1 + 10

print(Number2)
print(Variable[6])
print(Variable[0:6])
Fruite = ["Apple", "banana", "Orange"]
print(Fruite[0])
Para = """
Hi
Hi
Hi

"""
print(Para)
print(len(Para))
print(Variable.strip())
print(Variable.upper())
print(Variable.lower())
print(Variable.replace('V', 'B' ))
print(Variable.split('a'))
print("Val" in Variable)
List = [6, 2, 3, 4, 5]
List.sort()
print(List)
List.sort(reverse=True)
print(List)
my_data = {
    "name": "aravindhan",
    "age ": "24"
}
print(my_data.get("name"))
a, b = 10, 20
if a == 10 and b == 20:
    print("correct")
if a == 10 or b == 30:
    print("correct")
else:
    print("incorrect")
age = 17
if age > 18:
    print( "you can vote")
elif age == 18:
    print("you can also vote")
else:
    print("you can't vote")
c, d, = 100, 200
if c == 200 or d == 300:
    print("correct")
    if d == 300:
        print("correct")
    else:
        print("incorrect")
else:
    print("incorrect")
def function():
    e, f, = 100, 200
    print(e + f)
function()
def function1(g, h):
    print(g+g-h)
function1(100, 500)
function1(500, 500)
def Hi(name):
    print("Hi," + name)
Hi("Aravindhan")










