# x=lambda a,b:a*b
# print(x(3,8))


# def recursion(k):
#     n=5
#     if k < n:  # Base Case Check
#         result = k + recursion(k +1)  # Recursive Call
#         print(f"Returning: {result} (k={k})")
#         return result  # Returning the result up the call stack
#     else:  # Base Case
#         return 0  # Stops recursion when k is no longer > 0

# # Test the function
# print("Recursion Example Results")
# recursion(1)

'''Python List Methods with Code Examples and Explanations
Below are the methods you listed, their usage, and sample code to demonstrate how they work.

1. append()
Description: Adds an element at the end of the list.
Explanation: The append() method adds the specified element (in this case, 4) to the end of the list.'''

# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)  # Output: [1, 2, 3, 4]  when append the is only one element

''' 
2. clear()
Description: Removes all the elements from the list.
Explanation: The clear() method empties the list, leaving it with no elements.'''

# my_list = [1, 2, 3]
# my_list.clear()
# print(my_list)  # Output: []

''' 
3. copy()
Description: Returns a copy of the list.
Explanation: The copy() method creates a new list with the same elements as the original, but they are independent.'''

# my_list = [1, 2, 3]
# my_copy = my_list.copy()
# print(my_copy)  # Output: [1, 2, 3]

''' 4. count()
Description: Returns the number of elements with the specified value.
Explanation: The count() method counts how many times the value 2 appears in the list.'''

# my_list = [1, 2, 2, 3, 2]
# print(my_list.count(2))  # Output: 3

'''
5. extend()
Description: Adds elements of a list (or any iterable) to the end of the current list.
Explanation: The extend() method appends all elements from another iterable (list [4, 5] in this case) to the current list.'''

# my_list = [1, 2, 3]
# my_list.extend([4, 5])
# adtinal=(23,12,45,90)
# my_list.extend(adtinal)
# my_list.extend({1,2,3,4,5})
# print(my_list)  #the list is extend the above all 
# # out put [1, 2, 3, 4, 5, 23, 12, 45, 90, 1, 2, 3, 4, 5]

''' 6. index()
Description: Returns the index of the first element with the specified value.
Explanation: The index() method returns the position of the first occurrence of the value 2.'''

my_list = [1, 2, 3, 2]
print(my_list.index(2))  # Output: 1
''' when more than one element in the list contain then use these method 
# List of items
# Using enumerate to get index and value'''

my_list = ['a', 'b', 'c']


for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
''' the out put is 
Index: 0, Value: a
Index: 1, Value: b
Index: 2, Value: c '''
for specific value is my_list = [1, 2, 2, 3, 3, 4]

# Find indices of the value 2

indices_of_2 = [i for i, value in enumerate(my_list) if value == 2]
print(indices_of_2)  # Output: [1, 2]




# '''7. insert()
# Description: Adds an element at the specified position.
# my_list = [1, 2, 3]
# my_list.insert(1, 'a')  # Insert 'a' at index 1
# print(my_list)  # Output: [1, 'a', 2, 3]
# Explanation: The insert() method inserts the value 'a' at the specified index 1.
# 8. pop()
# Description: Removes the element at the specified position (or the last element if no index is specified).
# python
# Copy code
# my_list = [1, 2, 3]
# removed_element = my_list.pop(1)  # Remove element at index 1
# print(my_list)  # Output: [1, 3]
# print(removed_element)  # Output: 2
# Explanation: The pop() method removes the element at index 1 and returns it.
# 9. remove()
# Description: Removes the first item with the specified value.
# python
# Copy code
# my_list = [1, 2, 3, 2]
# my_list.remove(2)  # Remove the first occurrence of 2
# print(my_list)  # Output: [1, 3, 2]
# Explanation: The remove() method deletes the first instance of the value 2.
# 10. reverse()
# Description: Reverses the order of the list.
# python
# Copy code
# my_list = [1, 2, 3]
# my_list.reverse()
# print(my_list)  # Output: [3, 2, 1]
# Explanation: The reverse() method reverses the list in place.
# 11. sort()
# Description: Sorts the list in ascending order by default.
# python
# Copy code
# my_list = [3, 1, 2]
# my_list.sort()
# print(my_list)  # Output: [1, 2, 3]
# Explanation: The sort() method arranges the list in ascending order. For descending order, you can use sort(reverse=True).
# Combining Multiple Methods
# Here’s an example that combines several methods:

# python
# Copy code
# my_list = [3, 1, 2]
# my_list.append(4)          # Add 4 to the end
# print(my_list)             # Output: [3, 1, 2, 4]

# my_list.sort()             # Sort the list
# print(my_list)             # Output: [1, 2, 3, 4]

# my_list.reverse()          # Reverse the list
# print(my_list)             # Output: [4, 3, 2, 1]

# my_list.remove(3)          # Remove the value 3
# print(my_list)             # Output: [4, 2, 1]

# my_list.insert(1, 5)       # Insert 5 at index 1
# print(my_list)             # Output: [4, 5, 2, 1]
# Conclusion
# Each of these methods provides useful functionality for manipulating lists in Python. Experimenting with these methods and combining them in different ways can help you become proficient in managing lists effectively. Let me know if you'd like further clarification or examples! 😊





# You said:
# in case of index() in the list eg my_list=[1,2,2,3,3,4] then find the index of 2
# ChatGPT said:
# When you use the index() method, Python will return the index of the first occurrence of the specified value. Here's how it works for your example:

# Code Example:
# python
# Copy code
# my_list = [1, 2, 2, 3, 3, 4]
# index_of_2 = my_list.index(2)
# print(index_of_2)  # Output: 1
# Explanation:
# The method my_list.index(2) searches for the value 2 in the list.
# It starts from the beginning of the list and stops as soon as it finds the first occurrence of 2.
# In your list [1, 2, 2, 3, 3, 4], the first 2 appears at index 1 (Python uses 0-based indexing).
# If You Want All Occurrences of 2:
# If you need the indices of all occurrences of 2, you can use a list comprehension:

# python
# Copy code
# my_list = [1, 2, 2, 3, 3, 4]
# indices_of_2 = [i for i, value in enumerate(my_list) if value == 2]
# print(indices_of_2)  # Output: [1, 2]
# Explanation of List Comprehension:
# enumerate(my_list) loops through the list with both the index (i) and value (value).
# The condition if value == 2 filters for elements equal to 2.
# The resulting list contains all indices where 2 appears.
# Let me know if you'd like additional help with this! 😊





