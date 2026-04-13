import numpy as np

def square(x):
    return x*x

s  = square(4)
print(s)

numbers = [1,2,3,4,5,6,7,8]

m = list(map(square, numbers))
print(m)


l = list(map(lambda x:x*x, numbers))
print(l)

numbers1 = [1,2,3]
numbers2 = [4,5,6]

added_numbers = list(map(lambda x,y:x+y, numbers1, numbers2))

print(added_numbers)


b = np.array(numbers1)
c = np.array(numbers2)
d = b + c
print(d)

words = ["apple", "banana", "cherry"]

upper_words = list(map(str.upper, words))
print(upper_words)

def get_name(person):
    return person["name"]

people = [{
    "name": "sarosh",
    "age": 22
},{
    "name": "krish",
    "age": 21
}]



q = list(map(get_name, people))

print(q)


def even(num):
    if num % 2==0:
        return True

p = even(24)

print(p)

lst = [1,2,3,4,5,6,7,8,9,10,11,12]

pick = list(filter(even, lst))
print(pick)


check= list(map(lambda x: x%2==0, lst))
print(check)


nu = [1,2,3,4,5,6,7,8,9]

greater_than_five = list(filter(lambda x: x>5, nu))
print(greater_than_five)


greater_5 = [x for x in nu if x > 5 and x%2==0]
print(greater_5)