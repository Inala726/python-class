name = 'king'
# print(name[0])

# sentence = """
# This is a girl I really like but
# religion is standing between us
# 
# """

school = "aptech port harcourt"

# for x in school:
#     print(x)

# if "Port" in school:
#     print("please specify")
# else:
#     print("faaakin' 'ell`")

message = "This is the place"

msg = "     hello"
# print(message[-5:-2])
# print(message.upper())
# print(message.strip())

ex = "Uche, Bimbo, Mario"
# print(ex.replace("Bimbo", "Ada"))
newStr = ex.split(",")
# print(newStr)
# print(type(newStr))

# String formatting
friend = "Zion"
txt = f"The most handsome guy in our class is {friend.upper()}"
price = 45
txt2 = f"the current price is {price: .2f} naira"

# print(txt2)

quantity = 3
unit_price = 400
total_sale = f"the total sale is : {quantity*unit_price}"
# print(total_sale)

user_name = "daniel, dog, door"
# print(user_name.count("d", 5, 9))

account_number = "adebayo"
# print(account_number.isascii())

def reverse_string(str):
    return str[::-1]

def is_palindrome(str):
    
    rev = str[::-1]
    if rev == str:
        return "is palindrome"
    return "not palindrome"   

# print(reverse_string("hello"))
print(is_palindrome("FOM"))