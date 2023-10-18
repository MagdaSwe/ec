#!/usr/bin/env python
# coding: utf-8

# # NumPy

# Read the links: https://numpy.org/doc/stable/user/quickstart.html  and https://numpy.org/doc/stable/user/basics.broadcasting.html  before solving the exercises. 

# In[2]:


import numpy as np


# ### Print out the dimension (number of axes), shape, size and the datatype of the matrix A.

# In[9]:


A = np.arange(1, 16).reshape(3,5)


# In[3]:


print(A.ndim)
print(A.shape)
print(A.size)
print(A.dtype)
print(A)


# ### Do the following computations on the matrices B and C: 
# * Elementwise subtraction. 
# * Elementwise multiplication. 
# * Matrix multiplication (by default you should use the @ operator).

# In[4]:


B = np.arange(1, 10).reshape(3, 3)
C = np.ones((3, 3))*2

print(B)
print(C)
print(B - C,    "  Sub")
print(B * C,    " Element product")


print(B @ C,    "  matrix product")



# In[ ]:





# In[6]:


### Do the following calculations on the matrix:
B = np.arange(1, 10).reshape(3, 3)
print(B)
# Exponentiate each number elementwise (use the np.exp function).
print("Exponentiate each number elementwise ",np.exp(B))

#Calculate the minimum value in the whole matrix. 

print("Calculate the minimum value in the whole matrix.-\n",B.min())

# Calculcate the minimum value in each row. 
#print(B)

print("min per row: \n",B.min(axis=0))

# Calculcate the minimum value in each column. 
#B = np.arange(1, 10).reshape(3, 3)
#print(B)
print("min per column \n",B.min(axis=1))


# Find the index value for the minimum value in the whole matrix (hint: use np.argmin).
#B = np.arange(1, 10).reshape(3, 3)
print("index value for the minimum value in the whole matrix \n",np.argmin(B))

# Find the index value for the minimum value in each row (hint: use np.argmin).
print("index value for the minimum value in each row \n",np.argmin(B, axis=0))


# Calculate the sum for all elements.
print("sum for all elements \n",B.sum())

#Calculate the mean for each column. 
print("mean for all elements \n",np.mean(B, axis=1))

# Calculate the median for each column. 
print("meadian for all elements \n",np.median(B, axis=1))
#print("meadian for all elements ",B.median())



# ### What does it mean when you provide fewer indices than axes when slicing? See example below.

# In[6]:


print(A)


# In[7]:


A[1]


# **Answer:**

# In[8]:


#Returnerar den andra raden man frågar efter enbart, då den första har idex 0


# ### Iterating over multidimensional arrays is done with respect to the first axis, so in the example below we iterate trough the rows. If you would like to iterate through the array *elementwise*, how would you do that?

# In[10]:


A


# In[10]:


A = np.arange(1, 16).reshape(3,5)
for i in A:
    print(i)


# In[13]:


for x in np.nditer(A):
    print(x)

    #in your solution, you use flatten and ravel, hop this is ok?


# ### Explain what the code below does. More specifically, b has three axes - what does this mean? 

# In[14]:


a = np.arange(30)
b = a.reshape((2, 3, -1))
print(a)
#print()

print(b)


# # Svar: 
# 1) Skapar en array  med 20 element, när man kör reshape för den så får man i detta fall. Vi gör att den blir en 2 dimensionell array, där den yttre dimensionen har 2 rader, som har 3 arrays i sig med 5 element. -1 räknar ut själv hur många kolumner det ska va
# NumPy is smart enough to use the original scalar value without actually making copies so that broadcasting operations are as memory and computationally efficient as possible.

# ### Broadcasting
# **Read the following link about broadcasting: https://numpy.org/doc/stable/user/basics.broadcasting.html#basics-broadcasting**

# # Remark on Broadcasting when doing Linear Algebra calculations in Python. 

# ### From the mathematical rules of matrix addition, the operation below (m1 + m2) does not make sense. The reason is that matrix addition requires two matrices of the same size. In Python however, it works due to broadcasting rules in NumPy. So you must be careful when doing Linear Algebra calculations in Python since they do not follow the "mathematical rules". This can however easily be handled by doing some simple programming, for example validating that two matrices have the same shape is easy if you for instance want to add two matrices. 

# In[16]:


m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([1, 1])

print(m1 + m2)

print(m1.shape)
print(m2.shape)
print("-----------------------------")
if m1.shape==m2.shape:
    print(m1 + m2)
else: 
    print("The two matrices cannot be added since they have not the same shape")


# ### The example below would also not be allowed if following the "mathematical rules" in Linear Algebra. But it works due to broadcasting in NumPy. 

# In[14]:


v1 = np.array([1, 2, 3])
print(v1 + 1)


# In[18]:


A = np.arange(1, 5).reshape(2,2)
print(A)

b = np.array([2, 2])
print(b,"\n")
print(A+b)


# # Linear Algebra Exercises

# The exercies are taken from the "Matrix Algebra for Engineers" by Chasnov: https://www.math.hkust.edu.hk/~machas/matrix-algebra-for-engineers.pdf .
# 
# Do the following exercises: 
# * Chapter 2, exercise 1-3.
# * Quiz on p.11, exercise 2. 
# * Chapter 6, exercise 1. 
# * Quiz on p.19, exercise 3. 
# 
# 
# * Chapter 10, exercise 1. 
# * Chapter 12 exercise 1. 
# 

# In[21]:


A = np.array([[2, 1, -1], [1, -1, 1]])
B = np.array([[4, -2, 1], [2, -4, -2]])

C = np.array([[1, 2], [2, 1]])
D = np.array([[3, 4], [4, 3]])

E = np.array([[1], [2]])

print(A)
print(B)
#print(2*B)
print(C)
print(D)
print(E)




# **Chap2. Question 1.**
# 
# **Write a function "add_mult_matrices" that takes two matrices as input arguments (validate that the input are of the type numpy.ndarray by using the isinstance function), a third argument that is either 'add' or 'multiply' that specifies if you want to add or multiply the matrices (validate that the third argument is either 'add' or 'multiply'). When doing matrix addition, validate that the matrices have the same size. When doing matrix multiplication, validate that the sizes conform (i.e. number of columns in the first matrix is equal to the number of rows in the second matrix).**
# 
# In this exercise, create a function that takes two matrices as input and either adds or multiplies them by specifying a argument as either 'add' or 'multiply'. Validate that both matrices taken as input are of the type ndarray (use the isinstance function).

# In[22]:


A = np.array([[2, 1, -1], [1, -1, 1]])
B = np.array([[4, -2, 1], [2, -4, -2]])
C = np.array([[1, 2], [2, 1]])
D = np.array([[3, 4], [4, 3]])
E = np.array([[1], [2]])

#print(isinstance(A, np.ndarray))
#print(isinstance(B, np.ndarray))

    
def add_mult_matrices(mat_1, mat_2, calc_method):
    if isinstance(A, np.ndarray) and isinstance(B, np.ndarray):
        if calc_method == "add":
            if mat_1.shape==mat_2.shape: 
                return mat_1+mat_2
            else:
                print("they are not the same dimensions so you cannot add")
                pass
        elif calc_method=="multiply":
            if mat_1.shape[1]==mat_2.shape[0]: 
                return mat_1 @ mat_2
            else: 
                print("Matrix shapes don't match")
        else:
            print("not valid method to calculate")
            pass
    else:
        print("this is not a valid array or dimensions are not the same")
        pass


# In[18]:


print("1: ",add_mult_matrices(B,A,"subtract"))
print("2: ",add_mult_matrices(3*C,E,"subtract"))
print("3: ",add_mult_matrices(A,C,"multiply"))
print("4: ",add_mult_matrices(C,D,"multiply"))
print("5: ",add_mult_matrices(C,B,"multiply"))


# **Chap2. Question 2**

# In[25]:


A = np.array([[1, 2], [2, 4]])
B = np.array([[2, 1], [1,3]])
C = np.array([[4, 3], [0, 2]])


def add_mult_matrices(mat_1, mat_2, calc_method):
    if isinstance(A, np.ndarray) and isinstance(B, np.ndarray):
        if calc_method == "add":
            if mat_1.shape==mat_2.shape: 
                return mat_1+mat_2
            else:
                print("they are not the same dimensions so you cannot add")
                pass
        elif calc_method=="multiply":
            if mat_1.shape[1]==mat_2.shape[0]: 
                return mat_1 @ mat_2
            else: 
                print("Matrix shapes don't match")
        else:
            print("not valid method to calculate")
            pass
    else:
        print("this is not a valid array or dimensions are not the same")
        pass


# In[29]:


print("A*B: \n",add_mult_matrices(A,B,"multiply"))
print("A*C: \n",add_mult_matrices(A,C,"multiply"))


# **Chap2. Question 3**

# In[21]:


A = np.array([[1, 1, 1], [1, 2, 3], [1, 3, 4]])
D = np.array([[2, 0, 0], [0, 3, 0], [0, 0, 4]])
print("A*D: \n",add_mult_matrices(A,D,"multiply"))
print("D*A: \n",add_mult_matrices(D,A,"multiply"))


# **Quiz p.11, Question 2**

# In[30]:


A = np.array([[1, -1], [-1, 1]])
B = np.array([[-1, 1], [1,-1]])

print(add_mult_matrices(A,B,"multiply"))


# **Chap 6. Question 1**

# In[38]:


A = np.array([[5, 6],[4, 5]])
B = np.array([[6, 4],[3, 3]])
 
# Calculating the inverse of the matrix
print("Invers A \n",np.linalg.inv(A))
print("Invers B \n",np.linalg.inv(B))

print(np.allclose(B @ np.linalg.inv(B), np.eye(2)))


# **Quiz p.19, Question 3**

# In[24]:


A = np.array([[2, 2],[1, 2]])
print(np.linalg.inv(A))
print("the answer is a")


# **Chap10. Question 1 a)**

# In[25]:


A = np.array([[3, -7, -2],[-3, 5, 1],[6, -4, 0]])
B = np.array([-7, 5, 2])
print(np.linalg.solve(A, B))


# **Chap10. Question 1 b)**

# In[33]:


A = np.array([[1, -2, 3],[-1, 3, -1],[2, -5, 5]])
B = np.array([1, -1, 1])
print(np.linalg.solve(A, B))


# In[ ]:





# **Chap 12. Question 1**

# In[37]:


A = np.array([[3, -7, -2],[-3, 5, 1],[6, -4, 0]])
B = np.array([[1,0,0],[0,1,0],[0,0,1]])
 
# Calculating the inverse of the matrix with adding the inverse matrix and solve the equations system or inverse method

print(np.linalg.solve(A, B))
print(np.linalg.inv(A))


# ### Copies and Views
# Read the following link: https://numpy.org/doc/stable/user/basics.copies.html

# **Basic indexing creates a view, How can you check if v1 and v2 is a view or copy? If you change the last element in v2 to 123, will the last element in v1 be changed? Why?**

# In[28]:


v1 = np.arange(4)
v2 = v1[-2:]
print(v1)
print(v2)


# In[29]:


#The base attribute of the ndarray makes it easy to tell if an array is a view or a copy. 
#The base attribute of a view returns the original array while it returns None for a copy.

v2[-1]=123
print("original: ",v1.base)
#v2.base

print(v1)
print(v2)

print("yes, it will change becuase The data buffer remains the same, so any changes made to a view reflects in the original copy. ")


# # SVAR:
# The base attribute of a view returns the original array while it returns None for a copy.
# print(v1.base)
# print(v2.base)

# In[30]:


# The last element in v1 will be changed aswell since v2 is a view, meaning they share the same data buffer.
v2[-1] = 123
print(v1)
print(v2)


# In[ ]:




