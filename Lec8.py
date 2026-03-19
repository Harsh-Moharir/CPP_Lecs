# def addition(a, b):
#     print(f"Result: {a + b}")

# def subtraction(a, b):
#     print(f"Result: {a - b}")

# def multiplication(a, b):
#     print(f"Result: {a * b}")

# def division(a, b):
#     if b == 0:
#         print("Error: Cannot divide by zero!")
#     else:
#         print(f"Result: {a / b}")

# while True:
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
#     val1 = float(input("Enter the first number: "))
#     val2 = float(input("Enter the second number: "))
#     choice = input("Enter your choice: ")
#     if choice == '1':
#         addition(val1, val2)
#     elif choice == '2':
#         subtraction(val1, val2)
#     elif choice == '3':
#         multiplication(val1, val2)
#     elif choice == '4':
#         division(val1, val2)
#     elif choice == '5':
#         print("Exiting the program.")
#         break
#     else:
#         print("Invalid choice. Please try again.")
        
# def outerfunction():
#     print("This is the outer function.")
    
#     def innerfunction():
#         print("This is the inner function.")
    
#     innerfunction()
# outerfunction()

# name = "Alice is the best programmer in the world"
# count = 1
# for i in name:
#     if i == 'a' or i == 'A':
#         count += 1
#     else:
#         continue
# print(f"The number of 'a' or 'A' in the string is: {count - 1}")


# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b',)
# print(init_tuple_a == init_tuple_b)


# init_tuple_a = '1', '2'
# init_tuple_b = ('3', '4',)
# print(init_tuple_a + init_tuple_b)


# l = [1, 2, 3]
# init_tuple = ('Python') * (l.__len__() - l[::-1][0])
# print(init_tuple)


# init_tuple = ('Python') * 3
# print(type(init_tuple))



# init_tuple = ('Python') * 3
# init_tuple[0] = 2
# print(type(init_tuple))


# init_tuple = ((1,2),) * 7
# print(len(init_tuple[3:8]))


# s=""
# s1=s.replace("difficult", "easy")
# print(s1)
# s="ababababababababab"
# s1=s.replace("a", "b")
# print(s1)


# city=input("Enter the name of a city: ")
# scity=city.strip()
# if scity == 'Hyderabad':
#     print("The city is Hyderabad.")
# elif scity == 'Bangalore':
#     print("The city is Bangalore.")
# elif scity == 'Chennai':
#     print("The city is Chennai.")
# else:
#     print("The city is not recognized.")


# s=[ i*i for i in range(1, 11)]
# print(s)

# val2=[i for i in s if i%2==0]
# print(val2)


# squares={x: x*x for x in range(1,6)}
# print(squares)



Doubles={x: 2*x for x in range(1,6)}
print(Doubles)