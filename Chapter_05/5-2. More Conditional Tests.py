#You don’t have to limit the number of tests you create to 10 . If you want to
#try more comparisons, write more tests and add them to conditional_tests.py .
#Have at least one True and one False result for each of the following:


#• Tests for equality and inequality with strings
car = 'renault'
car == 'renault'
car == 'bmw'

#• Tests using the lower() function
car = 'Mercedes'
car.lower() == 'mercedes'

#• Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
#• Tests using the and keyword and the or keyword
my_age = 42
her_age = 32
\
my_age < her_age
my_age > her_age
my_age >= her_age and her_age <= my_age
my_age == 43 or her_age >= 30

#• Test whether an item is in a list
visited_cities = ['madrid', 'sevilla', 'valencia']
'madrid' in visited_cities

#• Test whether an item is not in a list
visited_cities = ['madrid', 'sevilla', 'valencia']
'barcelona' in visited_cities
