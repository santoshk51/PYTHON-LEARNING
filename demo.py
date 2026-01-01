x = int("10")
# print(type(x))

y = str(25)
# print(type(y))

txt = "python"


txt.lower()
# print(txt.upper())
# print(text[1:5])
l = "ot"
print(txt.replace("pyth", "jio"))
print(txt.startswith(l))

t = "hello world with chai"
print(t.split())
print(t.find("ai"))

## operation in python

a = 10
b = 21
print(b ** a)


# comparison operations

y = 20
z = 33

f = x == y
f1 = x != y
f2 = x > y
f3 = x < y
f4 = x >= y
f5 = x <= y

# print(f)
# print(f1)
# print(f2)
# print(f3)
# print(f4)
# print(f5)


# Membership & Identity operators

lst = [1,2,3,4,5]
lst1 = [1,2,3,4,5]
x =5

print(lst is not lst1)

# name  = input("Enter your name: ")
# print("Hello", name)

#Type conversion

age = int(input("Enter your age: "))
price = float(input("Enter the price: "))
print(age,"", price)

result = 10 + 2 * 3 # Multiplication happens first: 10 + (2 * 3) = 16
print(result)
result = (10 + 2) * 3 # Parentheses first: (10 + 2) * 3 = 36
print(result)
result = 2 ** 3 ** 2 # Right-to-left exponentiation: 2 ** (3 ** 2) = 2 ** 9 = 512
print(result)