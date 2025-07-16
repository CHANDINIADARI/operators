#!/usr/bin/env python
# coding: utf-8

# In[7]:


# --- 1. Arithmetic Operators ---
print("--- Arithmetic Operators ---")
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")       
print(f"Subtraction (a - b): {a - b}")    
print(f"Multiplication (a * b): {a * b}") 
print(f"Division (a / b): {a / b}")       
print(f"Floor Division (a // b): {a // b}") 
print(f"Modulus (a % b): {a % b}")       
print(f"Exponentiation (a ** b): {a ** b}")

print("\n")


# In[8]:


# --- 2. Comparison (Relational) Operators ---
print("--- Comparison Operators ---")
x = 15
y = 10

print(f"x = {x}, y = {y}")
print(f"Equal to (x == y): {x == y}")         
print(f"Not equal to (x != y): {x != y}")     
print(f"Greater than (x > y): {x > y}")       
print(f"Less than (x < y): {x < y}")         
print(f"Greater than or equal to (x >= y): {x >= y}") 
print(f"Less than or equal to (x <= y): {x <= y}")  

print("\n")


# In[9]:


# --- 3. Assignment Operators ---
print("--- Assignment Operators ---")
c = 5
print(f"Initial value of c: {c}")

c += 3  # c = c + 3
print(f"c after c += 3: {c}")  

c -= 2  # c = c - 2
print(f"c after c -= 2: {c}")  

c *= 4  # c = c * 4
print(f"c after c *= 4: {c}")  

c /= 3  # c = c / 3
print(f"c after c /= 3: {c}")  

c //= 2 # c = c // 2
print(f"c after c //= 2: {c}") 

c %= 3  # c = c % 3
print(f"c after c %= 3: {c}")  

c **= 2 # c = c ** 2
print(f"c after c **= 2: {c}") 

print("\n")


# In[11]:


# --- 4. Logical Operators ---
print("--- Logical Operators ---")
p = True
q = False

print(f"p = {p}, q = {q}")
print(f"Logical AND (p and q): {p and q}")
print(f"Logical OR (p or q): {p or q}")   
print(f"Logical NOT (not p): {not p}")   


# In[12]:


# --- 5. Identity Operators ---
print("--- Identity Operators ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1: {list1}, list2: {list2}, list3: {list3}")
print(f"list1 is list2: {list1 is list2}")   
print(f"list1 is list3: {list1 is list3}")  
print(f"list1 is not list2: {list1 is not list2}") 

print("\n")


# In[13]:


# --- 6. Membership Operators ---
print("--- Membership Operators ---")
my_string = "Hello Python"
my_list = [10, 20, 30, 40, 50]

print(f"my_string: '{my_string}', my_list: {my_list}")
print(f"'Python' in my_string: {'Python' in my_string}") 
print(f"'Java' in my_string: {'Java' in my_string}")   
print(f"30 in my_list: {30 in my_list}")         
print(f"60 in my_list: {60 in my_list}")         
print(f"100 not in my_list: {100 not in my_list}") 

print("\n")


# In[14]:


# --- 7. Bitwise Operators (for integers) ---
print("--- Bitwise Operators ---")
num1 = 10  
num2 = 4 

print(f"num1 = {num1} ({bin(num1)}), num2 = {num2} ({bin(num2)})")
print(f"Bitwise AND (num1 & num2): {num1 & num2} ({bin(num1 & num2)})")
print(f"Bitwise OR (num1 | num2): {num1 | num2} ({bin(num1 | num2)})")   
print(f"Bitwise XOR (num1 ^ num2): {num1 ^ num2} ({bin(num1 ^ num2)})") 
print(f"Bitwise NOT (~num1): {~num1} ({bin(~num1)})")  
print(f"Left Shift (num1 << 2): {num1 << 2} ({bin(num1 << 2)})") 
print(f"Right Shift (num1 >> 2): {num1 >> 2} ({bin(num1 >> 2)})")

