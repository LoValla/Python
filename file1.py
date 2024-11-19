x = 36 #int
y = 25.2 #float
z1 = 2.3 + 0.5j #complex
z2 = 1.8 + 3.1j #complex


print(f'x = {x} and y = {y}') #only for new python versions
print('x = {} and y = {}'.format(x, y)) #general use

print(z1 - z2)
print(z1 * z2)

a, b = 10, 4
print(f'a/b = {a/b} (standard ratio)')
print(f'a//b = {a//b} (integer part)')
print(f'a%b = {a%b} (rest)')

w1 = 'hello' + 'hello' #can sum strings (and even multiply)
print(w1, len(w1), w1[3])

s = 'It is rainy today'
list_words = s.split(' ')
print(list_words)

for w in s.split(' '):
    print(w, len(w))
    
# list: standard container
# tuple: unmodifiable list
# set: unordered list
# dictionary: list with a string associated to each item

#METHODS:
# number of items: len(my_list)
# loop over items: for element in my_list: ...
# check if a item is in the list: element in my_list
# get the ith element: my_list[i]
# get the sublist from element ith to jth: my_list[i:j]
# take only one element every n until j: my_list[i:j:n] ( elements of index i + p × n until j, with p = 0, 1, 2, ...)