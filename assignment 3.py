#!/usr/bin/env python
# coding: utf-8

# In[1]:


test_list = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483),
             ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_list = sorted(test_list, key=lambda x: x[1])
print("The sorted list is : ", sorted_list)


# In[2]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = map(lambda x: x**2, numbers)
squares_list = list(squares)
print("The squares of the numbers are:", squares_list)


# In[3]:


original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
string_tuple = tuple(map(lambda x: str(x), original_list))
print("Original list:", original_list)
print("Tuple of strings:", string_tuple)


# In[4]:


from functools import reduce
numbers = range(1, 26)
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers from 1 to 25:", product)


# In[5]:


numbers = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
def is_divisible_by_2_and_3(n):
  return n % 2 == 0 and n % 3 == 0
filtered_numbers = filter(is_divisible_by_2_and_3, numbers)
filtered_list = list(filtered_numbers)
print("Numbers divisible by 2 and 3:", filtered_list)


# In[6]:


strings = ['python', 'php', 'aba', 'radar', 'level']
is_palindrome = lambda s: s == s[::-1]
palindromes = filter(is_palindrome, strings)
palindrome_list = list(palindromes)
print("Palindromes:", palindrome_list)


# In[ ]:




