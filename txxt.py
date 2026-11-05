a = int(input("enter an integer:"))
b = float(input("enter a floating point number:"))
c = input("enter a string:")
d = bool(int(input("enter a boolean value(1 for true, 0 for false)")))

print("\nValues nd datatypes")
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

add = a + b
sub = a - b
mul = a * b
div = a / b
print("addition :",add)
print("substraction:",sub)
print("multiplication :",mul)
print("division :",div)

print("\nString operations")
print("concatenation:", c+ "python")
print("repetition:", c * 2)
print("length:", len(c))



