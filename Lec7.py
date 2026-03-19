# message = input()

# count = 0

# for ch in message:
#     if not ch.isalnum():
#         count += 1

# print(count)


# def count_special_and_spaces(text):
#     count = 0
#     for ch in text:
#         if not ch.isalnum():   # not a letter or digit
#             count += 1
#     return count

# message = input("Enter a message: ")

# result = count_special_and_spaces(message)
# print(result)


# import re
# var = 'gasgg54@#vscsd!s*'
# count = 0
# for i in var:
#     #z = re.findall(r'[a-zA-Z0-9]', i)
#     z = ord(i)
#     #print(z)
#     if z>=97 and z<=122:
#         continue
#     elif z>=48 and z<=57:
#         continue
#     else:
#         count += 1
# print(count)


# arr = list(map(int, input().split()))

# pos = 0  # position to place next non-zero

# for i in range(len(arr)):
#     if arr[i] != 0:
#         arr[pos], arr[i] = arr[i], arr[pos]
#         pos += 1

# print(*arr)


# arr = list(map(int, input().split()))

# largest = second = float('-inf')

# for num in arr:
#     if num > largest:
#         second = largest
#         largest = num
#     elif num > second and num != largest:
#         second = num

# print(second)

