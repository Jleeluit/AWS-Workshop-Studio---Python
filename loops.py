#A simmple loop

>>> fruit = ['apples','oranges','bananas']

>>> for item in fruit:
...     print(f'The best fruit now is {item}')

#The output should look like this
The best fruit now is apples
The best fruit now is oranges
The best fruit now is bananas

#If you want to want to use a loop as a counter, you could create a list of numbers and assign it to a variable like this.
numbers = [0,1,2,3,4,5,6,7,8,9,10]

#and then run
>>> numbers = [0,1,2,3,4,5,6,7,8,9,10]
>>> for number in numbers:
...     print(f'The next number is {number}')


#Which would print all the numbers from 0 to 10, but what if you wanted to count to 1000. It would be tedious to write all the numbers out in this way.
>>> for number in range(10):
...     print(f'The next number is {number}')


#Your output should look like this:
The next number is 0
The next number is 1
The next number is 2
The next number is 3
The next number is 4
The next number is 5
The next number is 6
The next number is 7
The next number is 8
The next number is 9

