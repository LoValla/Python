x = [1, 2, 3]
y = x  # CREATES A REFERENCE!!
y.append(4)
print(x)  # Output: [1, 2, 3, 4]

x = [1, 2, 3]
z = x.copy()  # NO REFERENCE, EXCEPT FOR NESTED OBJECTS
z.append(4)
print(x)  # Output: [1, 2, 3]

import copy

x = [2, 5, 6]
n = copy.deepcopy(x)  # USE FOR NESTED OBJECTS
print(n)

# In python, function must be defined before being used.
# The type of the arguement is not fixed so the same instruction will
# be interpreted differently depending on the type.


# Definition syntax
def function(argument):
    """my function documentation

    Arguments:
        argument (type): my argument description

    Returns:
        type: my result description
    """
    result = argument * 3
    return result


# Same function, two different types (int and string)
print("function(10) = {}".format(function(10)))
print("function('ouh') = {}".format(function("ouh")))
# help(function) is used to get documentation

# ARBITRARY NUMBER OF ARGUMENTS: *args and **kwargs
# *args: a bunch of values
# **kwargs: keyword arguments (e.g name="Lorenzo", age="24"), i.e. key+value.
# You can also first pack the arguments in a dictionary, then pass them to the function with **kwargs


def find_mean(*args):
    return sum(args) / len(args)


numbers = [2.3, 4.6, 10.9]
mean = round(find_mean(*numbers), 2)  # need to unpack to pass the list as *args
print(mean)
