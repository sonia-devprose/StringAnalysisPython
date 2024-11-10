def is_even(num):
 return num % 2 == 0

subtract = lambda a, b: a - b

old_list = [1,2,3,4,5,6,7,8]
# List comprehension
even_numbers = list(filter(is_even, old_list))
# new_list = [is_even(item) for item in old_list ]
# even_numbers = list(filter(is_even, num_list))
print(even_numbers)
new_tuple = ('x','y', 'z')
print(f"The 3D coordinates are {new_tuple}")
word = "character count example"
from collections import Counter
freq_char = Counter(word)
print(f"The count of frequency of each characters are: {freq_char}")