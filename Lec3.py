# #WAP to accept 3 paper marks and check minimum marks using nested if else

# marks1 = float(input("Enter marks for paper 1: "))
# marks2 = float(input("Enter marks for paper 2: "))
# marks3 = float(input("Enter marks for paper 3: "))
# if marks1 < marks2:
#     if marks1 < marks3:
#         print(f"Minimum marks is {marks1} in paper 1")
#     else:
#         print(f"Minimum marks is {marks3} in paper 3")
# else:
#     if marks2 < marks3:
#         print(f"Minimum marks is {marks2} in paper 2")
#     else:
#         print(f"Minimum marks is {marks3} in paper 3")

# #WAP to accept percentange and if it is greater than or equal to 90 then print A grade, if it is greater than or equal to 80 then print B grade, if it is greater than or equal to 70 then print C grade, if it is greater than or equal to 60 then print D grade otherwise print F grade
# percentage = float(input("Enter percentage: "))
# if percentage >= 90:
#     print("Grade: A")
# elif percentage >= 80:
#     print("Grade: B")
# elif percentage >= 70:
#     print("Grade: C")
# elif percentage >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")


# #indexing and slicing are not possible in dictionary 
# mydict = {"name": "John", "age": 30, "city": "New York"}
# print(mydict["name"]) #accessing value using key''==
# print(mydict.get("age")) #accessing value using get method
# mydict["age"] = 31 #updating value
# print(mydict) #printing the dictionary
# mydict["country"] = "USA" #adding new key-value pair
# print(mydict) #printing the dictionary
# del mydict["city"] #deleting key-value pair
# print(mydict) #printing the dictionary

# mydict = {101: "John", 102: "Jane", 103: "Doe"}
# print(mydict)

# for x in mydict:
#     print(x) #printing keys
     

# name="harsh"
# print(name[0])
# print(name[1])
# print(name[-1])

# s = "help4code is a best platform for learning python"
# print(s.find("best"))
# print(s.find("python"))
# print(s.find("learning"))
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# print('Subjects Marks:')
# phy=50
# chem=60
# maths=70
# print("physics={} chemistry={} maths={}".format(phy,chem,maths))
# print("physics={0} chemistry={1} maths={2}".format(phy,chem,maths))
# print("physics={x} chemistry={y} maths={z}".format(phy,chem,maths))
# total=phy+chem+maths
# print("Total marks={}".format(total))


# print('harsh333'.isalnum())
# print('harsh'.isalpha())
# print('12345'.isdigit())
# print(' '.isspace())
# print('Harsh'.isupper())
# print('harsh'.islower())
# print('Harsh'.istitle())
# print('Harsh'.isprintable())

name = "harsh"
data = ['a','e','i','o','u']
vowels = 0
con = 0
for i in name:
    if i in data:
        vowels += 1
    else:
        con += 1
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {con}")

