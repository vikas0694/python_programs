# characterCount

message = "hello this is vikas , and I am from bangalore."
count = {}

for i in message:
    count.setdefault(i, 0)
    count[i] = count[i] + 1

print(count)

