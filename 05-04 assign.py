'''1) given data1 = [-20,12,-55,-22,50,-50,-9,89,-224,67,10,-20,-22,8,-9,-5,-55]
find how many unique negative numbers are there
find their sum and avg
use lambda'''


data1 = [-20, 12, -55, -22, 50, -50, -9, 89, -224, 67, 10, -20, -22, 8, -9, -5, -55]
negative_numbers = list(filter(lambda x: x < 0, data1))
unique_negative_numbers = set(negative_numbers)
sum_neg = sum(unique_negative_numbers)
avg_neg = sum_negative / len(unique_negative_numbers) if unique_negative_numbers else 0

print("Unique negative numbers:", unique_negative_numbers)
print("Sum of unique negative numbers:", sum_neg)
print("Average of unique negative numbers:", avg_neg)

import random
from functools import reduce
data1 = [-20, 12, -55, -22, 50, -50, -9, 89, -224, 67, 10, -20, -22, 8, -9, -5, -55]
random_number = random.randint(10, 99)
data1_with_random = list(map(lambda x: x + random_number, data1))
sum_all = reduce(lambda x, y: x + y, data1_with_random)
avg = sum_all / len(data1_with_random)
highest = max(data1_with_random)
lowest = min(data1_with_random)
print("Random number generated:", random_number)
print("Data1 with random number added:", data1_with_random)
print("Sum of all numbers:", sum_all)
print("Average of all numbers:", avg)
print("Highest number:", highest)
print("Lowest number:", lowest)

