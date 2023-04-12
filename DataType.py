#Data Type from AWS Workshop Studio

#Using Number Variables in String

my_int = 50
sentence = "The total comes to: "

print(sentence + my_int)

#Dictionaries is a way of storying related inforamtion in key-value pairs

#Create 

>>> user = {"first_name":"Ada"}
>>> print(user)
{'first_name': 'Ada'}


#Delete a Key - Value Pair

>>> del user["family_name"]
>>> print(user)
{'first_name': 'Ada'}


#Organize a List 

>>>print(sorted(fruit))
['apples', 'bananas', 'kiwi', 'oranges', 'passion fruit']
>>>print(fruit)
['apples', 'oranges', 'passion fruit', 'bananas', 'kiwi']


#Determining Type
>>>my_variable = "A string"
>>>print(type(my_variable))
