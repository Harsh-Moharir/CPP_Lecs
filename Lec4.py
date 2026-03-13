# for i,j in zip(range(1,6),range(5,0,-1) ):
#     if i == 3 and j == 3:
#         continue
#     print(i,"",j)

# i=1
# while i<=5 :
#     print(i)
#     i+=1

# username=""
# password=""
# while username!="admin" and password!="admin123" :
#     username=input("Enter username:")
#     password=input("Enter password:")

# n=int(input("Enter a number: "))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1   
# print(f"The sum of first {n} natural numbers is: {sum}")

# name= "harsh"

# new_name = " "

# for i in name:
#     if i not in new_name:
#         new_name+=i

# print(name)
# print(new_name)

# mycart=[10,20,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("This is my purchased item")
#         continue
#     print(i)

# user_input = input("Enter a string: ")
# cleaned = user_input.replace(" ", "").lower()

# if cleaned == cleaned[::-1]:
# 	print("Palindrome")
# else:
# 	print("Not a palindrome")   

# first = input("Enter first string: ")
# second = input("Enter second string: ")

# clean_first = "".join(ch.lower() for ch in first if ch.isalnum())
# clean_second = "".join(ch.lower() for ch in second if ch.isalnum())

# if sorted(clean_first) == sorted(clean_second):
# 	print("Valid anagram")
# else:
# 	print("Not a valid anagram")


# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# if sorted(str1) == sorted(str2):
#     print("Valid anagram")


# def remove_harsh_key(my_dict):
# 	my_dict.pop("harsh", None)
# 	return my_dict


# my_dict = {"name": "Aman", "harsh": 95, "age": 20}
# print(remove_harsh_key(my_dict))


# for i in range(1, 4):
#     for j in range(1, 4):
#             print("j", end='')
#     print()



# n=int(input("Enter the number of rows: "))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(chr(64 + i), end=' ')
#     print()



n=int(input("Enter the number of rows: "))
for i in range (1, n + 1):
    for j in range(1, n + 1):
        print(n+1-i, end=' ')
    print()