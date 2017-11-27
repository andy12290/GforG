# string are immutable we cannot change the string once u declare
# but we can add with new variable.

a = 'Geeks'
print(a)
print(a+'for')

# other factor is we can access the string by aceesing the particuler element
# like array
print(a[1:3])

# String find and rfind
str = "geeksforgeeks is for geeks"
str2 = "geeks"
print(len(str2))
print(str.find(str2))

# Starts with function to check the Starts
# same we can do with the other as well.
str = "geeksforgeeks"
str1 = "geeks"

if str.startswith(str1):
    print('True')
else:
    print('False')


# lower and upper function

# Python code to demonstrate working of
# isupper() and islower()
str = "GeeksforGeeks"
str1 = "geeks"
if str.isupper():
    print('All character in upper')
else:
    print('Not all chr in upper case')
       
