# a = int(input("please enter three digit number : "))

# b = a % 10
# print(b)
# c = a//10
# print(c)
# d = c%10
# print(d)

# e = c//10
# print(e)
# f = e%10
# print(f)
# g = e//10
# print(g)
# print(b + d + f + g)


name = "vikas ujjwal bangalore bhopal "
char = {}

for i in name:
    char.setdefault(i, 0)
    char[i] = char[i] + 1

print(char) 
