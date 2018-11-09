#tupel
# mixed = (1,2,3,4,5.0)
#
# for i in mixed:
#     print(i)
#
# tupel is a data structure type which uses for data storage

num = ("vikas")
print(type(num))

num1 = (1,)
words = ('word1')
print(type(num1))
print(type(words))


num3 = tuple(range(1,11))
print(num3)

num2 = list(range(0,11))
print(num2)



mixed = (1,2,3,4,5, [6,7,8])
mixed[5].pop(0)
print(mixed)