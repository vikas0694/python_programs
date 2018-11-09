# # dictionaries

#
# pop meth# add and delete data

user_info = {
    'name' : 'vikas',
    'age' : 23,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale'],
}

# # how to add data
user_info['fav_songs'] = ['song1', 'song2']
print(user_info)

#
# # pop method
popped_item = user_info.pop('age')
print(type(popped_item))
print(user_info)


# pop item method
popped_item = user_info.popitem()
print(user_info)
print(type(popped_item))
popitem method
popped_item = user_info.popitem()
print(user_info)
print(type(popped_item))

more_info = {'state' : 'west bengal', 'in' : [ 'home','brother', 'learn']}
user_info.update(more_info)
print(user_info)
