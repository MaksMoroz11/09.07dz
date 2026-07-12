# 1
# Программа 1
name = "Alex 22.3"
number = 22.3

# Программа 2
number = 22.3
name = "Alex " + str(number)


# 2
# Программа 1
name = "Alex"
def print_hello():
    print("Hello")

# Программа 2
def print_hello():
    print("Hello")
name = "Alex"


# 3
# Программа 1
items = ["Hello", "Bye", 1]
lst = items
a = "Bye"

# Программа 2
items = ["Hello"]
items.append("Bye")
items.append(1)
lst = items
a = "Bye"


# 4
# Программа 1
lst_1 = ["Hello", 1]
lst_2 = ["Hello", 1]
lst_3 = ["Hello"]

# Программа 2
hello = "Hello"
one = 1
lst_1 = [hello, one]
lst_2 = [hello, one]
lst_3 = [hello]


# 5
# Программа 1
user = {"id": 1, "name": "Test"}
data = {"users": [user]}
user_copy = user

# Программа 2
user_copy = {"id": 1, "name": "Test"}
user = user_copy
data = {"users": [user]}


# 6
# Программа 1
array = [[1, 2], [3, 4]]
array_copy = array
array_deepcopy = [[1, 2], [3, 4]]

# Программа 2
inner1 = [1, 2]
inner2 = [3, 4]
array = [inner1, inner2]
array_copy = array
new_inner1 = [1, 2]
new_inner2 = [3, 4]
array_deepcopy = [new_inner1, new_inner2]
