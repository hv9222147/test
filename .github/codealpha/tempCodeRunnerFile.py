
def palindrome(string):
    string = string.lower()
    reversed_string = string[:: -1]
    if string == reversed_string:
        return True
    else:
        return False
string = input("enter a string: ")
result = palindrome(string)
print("the string is palindrome:",result)

