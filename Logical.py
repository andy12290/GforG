# Logical operator on String
# only and and OR work on string
# Empty string represent the False string in  python

line = "Geek1 \nGeek2 \nGeek3";
# splitting string by delimeter
print(line.split()) # normal splitting
print(line.split(' ',1))


# Formatting
variable = '15'
s = ('variable are string= %s' %variable)
print(s)

# we will convert and again will file
variable = int(variable)
s = ('variable are string= %d' %variable)
print(s)
