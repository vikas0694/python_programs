# find birthday
birthdays = {'vikas': 'Sep 6', 'ujjwal': 'Dec 12', 'aditya': 'Nov 11'}

while True:
    print('Enter a name: (blank to stop)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')