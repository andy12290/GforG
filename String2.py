# number of character in String
str = "geeksforgeeks is for geeks"
print(str.count("geeks",0,15))

# python working with join function
# Python code to demonstrate working of
# join()
str = "_"
str1 = ( "geeks", "for", "geeks" )
print(str.join(str1))

# lstrip rstrip and
str = "---geeksforgeeks---"
#print("After stripping the:", str.strip('-'), end='')


# replace method in String
str = "nerdsfornerds is for nerds"
str1 = "nerds"
str2 = "geeks"
print("After replacing the string: ",str.replace(str1,str2))
