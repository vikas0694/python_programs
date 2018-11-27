# csv files
import csv
 with open(r"C:\Users\vikas\Desktop\new1.csv","w") as csvfile:
     fieldnamessage = ['Grade','first_name','last_name']
     writer = csv.DictWriter(csvfile,fieldnames = fieldnamessage)
     writer.writeheader()
     writer.writerows([{'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'},{'Grade': 'A', 'first_name': 'Rachael',
                        'last_name': 'Rodriguez'},
                       {'Grade': 'C', 'first_name': 'Ali', 'last_name': 'Hassan'},
                       {'Grade': 'B', 'first_name': 'Annas', 'last_name': 'Lakhany'},
                       {'Grade': 'A', 'first_name': 'Babu', 'last_name': 'Lal'}])

print("file created")


# to read csv file

# import csv
# with open(r"C:\Users\vikas\Desktop\new1.csv","r") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['Grade'],row['first_name'],row['last_name'])


# next(filereader) -> to remove file collum name

# to remove   csv file

# import os
# os.remove(r"enter path here")


