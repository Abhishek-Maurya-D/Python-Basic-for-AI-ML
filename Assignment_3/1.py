string = str(input("Enter the String: "))

#Build in function

# string2 = string[::-1]
# if string == string2:
#     print("The given string is a palindrome")
# else:
#     print("The given string is not a palindrome")

# Without using build in function

is_palindrome = True
start = 0
end = len(string)
while end>=start:
    if(string[start] == string[end-1]):
        start += 1
        end -= 1
    else:
        is_palindrome = False
        break;
if(is_palindrome == True):
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")