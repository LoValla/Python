x = 36  # int
y = 25.2  # float
z1 = 2.3 + 0.5j  # complex
z2 = 1.8 + 3.1j  # complex


print(f"x = {x} and y = {y}")  # only for new python versions
print("x = {} and y = {}".format(x, y))  # general use

print(z1 - z2)
print(z1 * z2)

a, b = 10, 4
print(f"a/b = {a/b} (standard ratio)")
print(f"a//b = {a//b} (integer part)")
print(f"a%b = {a%b} (rest)")

w1 = "hello" + "hello"  # can sum strings (and even multiply)
print(w1, len(w1), w1[3])

s = "It is rainy today"
list_words = s.split(" ")
print(list_words)

for w in s.split(" "):
    print(w, len(w))

# list: standard container
# tuple: unmodifiable list
# set: unordered list
# dictionary: list with a string associated to each item

# METHODS:
# number of items: len(my_list)
# loop over items: for element in my_list: ...
# check if a item is in the list: element in my_list
# get the ith element: my_list[i]
# get the sublist from element ith to jth: my_list[i:j]
# take only one element every n until j: my_list[i:j:n] ( elements of index i + p × n until j, with p = 0, 1, 2, ...)

l = [1, 3, 7]  # list initialisation

my_list = [1, 3.2, 4.1, "banana", "string", 1 + 3j, [100, 1000]]  # x = [] initialises a list
for element in my_list[6:0:-1]:  # -1 -> prints the list backwards
    print("{} is {}".format(element, type(element)))

print("Is 'banana' in the list? {}".format("banana" in my_list))

t = (1, 3, 7)  # tuple initialisation

s = {1, 3, 7}  # set initialisation
try:
    print(s[1])
except TypeError:
    print("Impossible to access element via indexing")  # set is unordered

person = {
    "name": "Charles",
    "age": 78,
    "size": 173,
    "gender": "M",
}  # dictionary initialisation (keys + values)
person["eyes"] = "blue"  # adding a key and its value
print(person["eyes"])

for v in person.values():  # loop over dictionary values only
    print(v)

for key, value in person.items():  # Loop over both keys and values directly
    print(f"{key}: {value}")

l = [1, 3, 7]
for idx, element in enumerate(l):
    if element < 4:
        print(f"{element} at index {idx}")

while len(my_list) > 0:  # erase one by one the list elements (from the end)
    my_list.pop()
    print(my_list)

# Comprehension list with a condition (e.g. keep only even numbers)
list_even = [i for i in range(0, 10) if i % 2 == 0]
print(list_even)

# Comprehension with nested loops
sum_integers = [i * 10 + j for i in range(0, 5) for j in range(0, 5)]
print(sum_integers)

# Using zip() (lists must have the same length)
l1, l2, l3 = range(0, 10), range(0, 100, 10), range(0, 1000, 100)
for i, j, k in zip(l1, l2, l3):
    print(i, j, k, i + j + k)