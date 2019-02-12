# # dictionaries
#  #
#  # how to add data
#

data
user_info = {
    'name' : 'vikas' ,
    'age' : '23',
    'movie' : ['lagaan, coco'],
    'song' : ['chalti ka naam gadi, music, gana'],
}
#     add and delete data

#
# how to add data
user_info['fav_songs'] = ['song1', 'song2']
print(user_info)


#
# pop method
popped_item = user_info.pop('age')
print(type(popped_item))
print(user_info)
# add and delete data
# how to add data
# user_info['fav_songs'] = ['song1', 'song2']
# print(user_info)