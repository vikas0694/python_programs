# characterCount

message = 'hello this is vikas , and I am from bangalore.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)