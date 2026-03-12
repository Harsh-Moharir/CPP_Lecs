math = 40
pi = 3.14
name = 'Kshitij Panday'
print(type(math))
print(type(pi))
print(type(name))


print(2+2)
print("2"+"2")

#try:
#	val1 = int(input("Enter the First Value:"))
#	val2 = int(input("Enter the Second Value:"))
#	print(val1+val2)
#except ValueError:
#	print("Error: Please enter valid integers")

#typcasting values for int 
print("typcasting values for int")
print(int(3.14))
print(int(True))
print(int(False))
print(int("4"))


#typcasting values for float
print("typcasting values for float")
print(float(3))
print(float(True))
print(float(False))
print(float(3.14))
print(float("3"))

#typcasting values for complex
print("typcasting values for complex")
print(complex(3))
print(complex(3.14))
print(complex("3"))
print(complex("3+4j"))
print(complex(True))
print(complex(False))
print(complex(True,False))
print(complex(5,-3))


#typcasting values for bool
print("typcasting values for bool")
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(0.0))
print(bool(0.1))
print(bool(""))
print(bool("Hello"))
print(bool(1+2j))


#WAP for simple interest 
print("\n#WAP for simple interest")
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period (in years): "))

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print(f"Simple Interest: {simple_interest}")
print(f"Total Amount: {total_amount}")


#WAP a program to maintain temperature in centigrade and fahrenheit
print("\n#WAP a program to maintain temperature in centigrade and fahrenheit")
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
temp_c = float(input("Enter temperature in Celsius: "))
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is equal to {temp_f}°F")
temp_f = float(input("Enter temperature in Fahrenheit: "))
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F is equal to {temp_c}°C")


#Program to take input from user for 2 numbers and then replacing first value with sencond value and second value with first value and then print the values of both the numbers after swapping.

val1 = input("Enter the First Value: ")
val2 = input("Enter the Second Value: ")

print("Before swapping:")
print(f"First Value: {val1}")
print(f"Second Value: {val2}")

# Swapping the values
val1, val2 = val2, val1

print("After swapping:")
print(f"First Value: {val1}")
# Swapping the values using temp variable
temp = val1
val1 = val2
val2 = temp

print("After swapping:")
print(f"First Value: {val1}")
print(f"Second Value: {val2}")


# Swapping without using a temporary variable
val1 = int(val1) + int(val2)
val2 = int(val1) - int(val2)
val1 = int(val1) - int(val2)

print("After swapping without temp variable:")
print(f"First Value: {val1}")
print(f"Second Value: {val2}")


#WAP to enter height of user in feet and convert it into inch and centimeter
height_feet = float(input("Enter height in feet: "))

height_inches = height_feet * 12
height_cm = height_feet * 30.48

print(f"Height in feet: {height_feet}")
print(f"Height in inches: {height_inches}")
print(f"Height in centimeters: {height_cm}")


#WAP to Reverse a 3 digit number with loop
num = int(input("eEnter a  number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(f"Reversed number with loop : {rev}")

#WAP to Reverse a 3 digit number without loop
num = 1234567
a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
num = num // 10
d = num % 10
num = num // 10
e = num % 10
num = num // 10
f = num % 10
num = num // 10
g = num % 10
rev = a * 1000000 + b * 100000 + c * 10000 + d * 1000 + e * 100 + f * 10 + g
print(f"Reversed number using sir's logic (without loop): {rev}")
#num =123
#a=num % 10
#num = num // 10
#b = num % 10
#num = num // 10
#c = num % 10
#rev = a * 100 + b * 10 + c
#print(f"Reversed number: {rev}")