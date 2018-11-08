def cube_finder(n):
    cube = {}
    for i in range(1,n+1):
        cube[i] = i**3
    return cube
a = int(input("enter a num :"))
print(cube_finder(a))