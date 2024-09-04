message = "Hello Python World!"
print(message)
message = "Python is my favorite language!"
print(message)
message = "Thank you for sharing Python with the world, Guido!"
print(message)
my_string = "This is a double-quoted string."
print(my_string)
quote = "Linus Torvalds once said, 'Any program is only as good as it is useful.'"
first_name = 'eric'
print(first_name)
print(first_name.title())
first_name = 'eric'
print(first_name)
print(first_name.title())
print(first_name.upper())
Introduction to Python
Contribute
Python Essentials
Projects
Resources

 
Variables, Strings, and Numbers
In this section, you will learn to store information in variables. You will learn about two types of data: strings, which are sets of characters, and numerical data types.

Previous: Hello World | Home | Next: Lists and Tuples

Contents
Variables
Example
Naming rules
NameError
Exercises
Strings
Single and double quotes
Changing case
Combining strings (concatenation))
Whitespace
Exercises
Numbers
Integer operations
Floating-point numbers
Integers in Python 2.7
Exercises
Challenges
Comments
What makes a good comment?
When should you write comments?
Exercises
Zen of Python
Overall Challenges
Variables
A variable holds a value.

Example
message = "Hello Python world!"
print(message)
A variable holds a value. You can change the value of a variable at any point.

message = "Hello Python world!"
print(message)

message = "Python is my favorite language!"
print(message)
Naming rules
Variables can only contain letters, numbers, and underscores. Variable names can start with a letter or an underscore, but can not start with a number.
Spaces are not allowed in variable names, so we use underscores instead of spaces. For example, use student_name instead of "student name".
You cannot use Python keywords as variable names.
Variable names should be descriptive, without being too long. For example mc_wheels is better than just "wheels", and number_of_wheels_on_a_motorycle.
Be careful about using the lowercase letter l and the uppercase letter O in places where they could be confused with the numbers 1 and 0.
NameError
There is one common error when using variables, that you will almost certainly encounter at some point. Take a look at this code, and see if you can figure out why it causes an error.

message = "Thank you for sharing Python with the world, Guido!"
print(mesage)
Let's look through this error message. First, we see it is a NameError. Then we see the file that caused the error, and a green arrow shows us what line in that file caused the error. Then we get some more specific feedback, that "name 'mesage' is not defined".

You may have already spotted the source of the error. We spelled message two different ways. Python does not care whether we use the variable name "message" or "mesage". Python only cares that the spellings of our variable names match every time we use them.

This is pretty important, because it allows us to have a variable "name" with a single name in it, and then another variable "names" with a bunch of names in it.

We can fix NameErrors by making sure all of our variable names are spelled consistently.

message = "Thank you for sharing Python with the world, Guido!"
print(message)
In case you didn't know Guido van Rossum created the Python language over 20 years ago, and he is considered Python's Benevolent Dictator for Life. Guido still signs off on all major changes to the core Python language.


Exercises
Hello World - variable
Store your own version of the message "Hello World" in a variable, and print it.
One Variable, Two Messages:
Store a message in a variable, and then print that message.
Store a new message in the same variable, and then print that new message.
top

Strings
Strings are sets of characters. Strings are easier to understand by looking at some examples.

Single and double quotes
Strings are contained by either single or double quotes.

my_string = "This is a double-quoted string."
my_string = 'This is a single-quoted string.'
This lets us make strings that contain quotations.

quote = "Linus Torvalds once said, 'Any program is only as good as it is useful.'"
Changing case
You can easily change the case of a string, to present it the way you want it to look.

first_name = 'eric'

print(first_name)
print(first_name.title())
It is often good to store data in lower case, and then change the case as you want to for presentation. This catches some TYpos. It also makes sure that 'eric', 'Eric', and 'ERIC' are not considered three different people.

Some of the most common cases are lower, title, and upper.

first_name = 'eric'

print(first_name)
print(first_name.title())
print(first_name.upper())

first_name = 'Eric'
print(first_name.lower())
You will see this syntax quite often, where a variable name is followed by a dot and then the name of an action, followed by a set of parentheses. The parentheses may be empty, or they may contain some values.

variable_name.action()

In this example, the word "action" is the name of a method. A method is something that can be done to a variable. The methods 'lower', 'title', and 'upper' are all functions that have been written into the Python language, which do something to strings. Later on, you will learn to write your own methods.

Combining strings (concatenation)
It is often very useful to be able to combine strings into a message or page element that we want to display. Again, this is easier to understand through an example.

first_name = 'ada'