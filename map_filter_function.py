#map function
number = [1,2,3,4]

def square(a):
    return a**2
squares = list(map(square, number))

print(square)

# Filter function

num = [1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda a:a%2==0, num))
print(even)
