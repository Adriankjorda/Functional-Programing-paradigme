
people = [
    {"name":"Paula Key", "age":23},
    {"name":"Riya Dickerson" , "age":99},
    {"name":"Layne Colon" , "age":53},
    {"name":"Pranav Giles" , "age":51},
    {"name":"Kamryn Davis" , "age":27},
    {"name":"Taniyah Yu" , "age":17},
    {"name":"Brendon Porter" , "age":23},
    {"name":"Jordin Hancock" , "age":86},
    {"name":"Shawn Vargas" , "age":88},
    {"name":"Sawyer Copeland" , "age":14},
    {"name":"Gustavo Baldwin" , "age":7},
    {"name":"Renee Wilson" , "age":29}
]

# printing the list
print(people)

# Task 1

print ("task 1")

def my_reduce(function, sequence):
    result = sequence[0]
    for item in sequence[1:]:
        result = function(result, item)
    return result

people = [
    {"name":"Paula Key", "age":23},
    {"name":"Riya Dickerson" , "age":99},
    {"name":"Layne Colon" , "age":53},
    {"name":"Pranav Giles" , "age":51},
    {"name":"Kamryn Davis" , "age":27},
    {"name":"Taniyah Yu" , "age":17},
    {"name":"Brendon Porter" , "age":23},
    {"name":"Jordin Hancock" , "age":86},
    {"name":"Shawn Vargas" , "age":88},
    {"name":"Sawyer Copeland" , "age":14},
    {"name":"Gustavo Baldwin" , "age":7},
    {"name":"Renee Wilson" , "age":29}
]

def count_people_above_age(age, people):
    count = 0
    for person in people:
        if person["age"] > age:
            count += 1
    return count

above_fifty = my_reduce(lambda a, b: a + b, [count_people_above_age(50, people)])
print("Number of people above the age of 50:", above_fifty)

# Task 2

print ("Task 2")

def forEach(lst, func):
    for item in lst:
        func(item)

def greet(people):
    print(f"Hi, {people['name']}!")

forEach(people, greet)

# Task 3

print ("task 3")

def my_map(func, arr):
    new_arr = []
    for item in arr:
        new_arr.append(func(item))
    return new_arr

def increment_age(person):
    person["age"] += 1
    return person

new_people = my_map(increment_age, people)
print(new_people)

# Task 4

print ("Task 4")

def my_filter(function, iterable):
    result = []
    for item in iterable:
        if function(item):
            result.append(item)
    return result

def is_under_drinking_age(person):
    return person['age'] < 18

under_drinking_age = my_filter(is_under_drinking_age, people)
print (under_drinking_age)
    
    
# Task 5

print ("Task 5")

def sum(numbers):
    result = 0
    for num in numbers:
        result += num
    return result

ages = map(lambda person: person["age"], people)
total_age = sum(ages)

print(total_age)
 
 # Task 6
 
print ("Task 6")

def average(lst):
    return sum(lst) / len(lst)

ages = [person["age"] for person in people]
avg_age = average(ages)
print(avg_age)

# Task 7

print ("Task 7")

def max(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[-1]


def min(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[0]


ages = list(map(lambda x: x["age"], people))
max_age = max(ages)
min_age = min(ages)

print("Maximum age:", max_age)
print("Minimum age:", min_age)