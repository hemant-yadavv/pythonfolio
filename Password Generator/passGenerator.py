import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

passLen = 12
charValues = string.ascii_letters + string.digits + string.punctuation
# print(charValues)

# password = ""
# for i in range(passLen):
#     password += random.choice(charValues)

# print("your password is : ",password)


#list comprehension
password = "".join([random.choice(charValues) for i in range(passLen)])
print("your password is : ",password)