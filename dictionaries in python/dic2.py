# Dictionaries 


d = {'name' : 'unknown', 'age' : 'unknown'}

d = dict.fromkeys(['name','age', 'height'], 'unknown')
print(d)
# get method

d1 = {'name': 'vikas', 'age': 'unknown'}
print(d['name'])

print(d.get('names'))
no error

if d.get('name'):
    print('present')
else:
    print('not present')

clear method
d.clear()
print(d)