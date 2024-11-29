#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


# In[2]:


#No.1
x = np.linspace(0, 10, 400)  
y1 = (12 - 2 * x) / 3  
y2 = (8 - x) / 2       

y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="2A + 3B <= 12")
plt.plot(x, y2, label="A + 2B <= 8")
plt.fill_between(x, 0, np.minimum(y1, y2), color="lightblue", alpha=0.5, label="Feasible Region")
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel("A (Product A)")
plt.ylabel("B (Product B)")
plt.title("Feasible Region for Factory Profit Maximization")
plt.legend()
plt.grid()
plt.show()

c = [-3, -4] 
A = [[2, 3], [1, 2]]
b = [12, 8]
bounds = [(0, None), (0, None)] 

result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
optimal_A, optimal_B = result.x

print(f"Optimal Solution: A = {optimal_A}, B = {optimal_B}")
print(f"Maximum Profit: Z = {-result.fun}")


# In[3]:


#No.2
x = np.linspace(0, 5, 400)  
y1 = (5 - x) / 2 
y2 = 6 - 2 * x    

y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)


plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="X + 2Y <= 5")
plt.plot(x, y2, label="2X + Y <= 6")
plt.fill_between(x, 0, np.minimum(y1, y2), color="lightblue", alpha=0.5, label="Feasible Region")
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel("X (Product X)")
plt.ylabel("Y (Product Y)")
plt.title("Feasible Region for Cost Minimization")
plt.legend()
plt.grid()
plt.show()

c = [2, 5]  
A = [[1, 2], [2, 1]]
b = [5, 6] 
bounds = [(0, None), (0, None)]  

result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
optimal_X, optimal_Y = result.x

print(f"Optimal Solution: X = {optimal_X:.2f}, Y = {optimal_Y:.2f}")
print(f"Minimum Cost: Z = {result.fun:.2f}")


# In[6]:


#No.3
x = np.linspace(0, 20, 400) 
y1 = 20 - 2 * x  
y2 = (30 - 3 * x) / 2 
y3 = (18 - x) / 2  

y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)
y3 = np.maximum(0, y3)


plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="2A + B <= 20")
plt.plot(x, y2, label="3A + 2B <= 30")
plt.plot(x, y3, label="A + 2B <= 18")
plt.fill_between(x, 0, np.minimum(np.minimum(y1, y2), y3), color="lightblue", alpha=0.5, label="Feasible Region")
plt.xlim(0, 15)
plt.ylim(0, 15)
plt.xlabel("A (Product A)")
plt.ylabel("B (Product B)")
plt.title("Feasible Region for Maximizing Production")
plt.legend()
plt.grid()
plt.show()

c = [-5, -4] 
A = [[2, 1], [3, 2], [1, 2]]  
b = [20, 30, 18]  
bounds = [(0, None), (0, None)] 

result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
optimal_A, optimal_B = result.x

optimal_A, optimal_B, result.fun


# In[8]:


#No.4
x = np.linspace(0, 20, 400) 
y1 = (20 - x) / 2  
y2 = (15 - x) / 2  


y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)


plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="A + 2B <= 20")
plt.plot(x, y2, label="A + 2B <= 15")
plt.fill_between(x, 0, np.minimum(y1, y2), color="lightblue", alpha=0.5, label="Feasible Region")
plt.xlim(0, 20)
plt.ylim(0, 10)
plt.xlabel("A (Product A)")
plt.ylabel("B (Product B)")
plt.title("Feasible Region for Maximizing Revenue")
plt.legend()
plt.grid()
plt.show()


c = [-4, -5] 
A = [[1, 2], [1, 2]]  
b = [20, 15] 
bounds = [(0, None), (0, None)] 

result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
optimal_A, optimal_B = result.x

optimal_A, optimal_B, result.fun


# In[9]:


#No.5
x = np.linspace(0, 5, 400) 
y1 = (12 - 3 * x) / 4 
y2 = 6 - 2 * x 


y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)


plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="3P1 + 4P2 <= 12")
plt.plot(x, y2, label="2P1 + P2 <= 6")
plt.fill_between(x, 0, np.minimum(y1, y2), color="lightblue", alpha=0.5, label="Feasible Region")
plt.xlim(0, 5)
plt.ylim(0, 6)
plt.xlabel("P1 (Project 1)")
plt.ylabel("P2 (Project 2)")
plt.title("Feasible Region for Resource Allocation")
plt.legend()
plt.grid()
plt.show()


c = [-8, -7] 
A = [[3, 4], [2, 1]]
b = [12, 6]
bounds = [(0, None), (0, None)]  

result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
optimal_P1, optimal_P2 = result.x

optimal_A, optimal_B, result.fun


# In[11]:


#No.6
x = np.linspace(0, 8, 400) 
y1 = (8 - x) / 2 
y2 = (12 - 3 * x) / 2 


y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)


plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="C + 2V <= 8")
plt.plot(x, y2, label="3C + 2V <= 12")
plt.fill_between(x, 0, np.minimum(y1, y2), color="lightblue", alpha=0.5, label="Feasible Region")
plt.xlim(0, 8)
plt.ylim(0, 6)
plt.xlabel("C (Chocolate Cakes)")
plt.ylabel("V (Vanilla Cakes)")
plt.title("Feasible Region for Bakery Production Planning")
plt.legend()
plt.grid()
plt.show()


c = [-5, -3] 
A = [[1, 2], [3, 2]] 
b = [8, 12]  
bounds = [(0, None), (0, None)] 


result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
optimal_C, optimal_V = result.x
optimal_value = result.fun  # Store the objective function value

optimal_C, optimal_V, optimal_value


# In[13]:


#No.7
x = np.linspace(0, 7, 400) 
y1 = (18 - 3 * x) / 4  
y2 = 10 - 2 * x 


y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="3X + 4Y <= 18")
plt.plot(x, y2, label="2X + Y <= 10")
plt.fill_between(x, 0, np.minimum(y1, y2), color="lightblue", alpha=0.5, label="Feasible Region")
plt.xlim(0, 7)
plt.ylim(0, 10)
plt.xlabel("X (Vehicle X)")
plt.ylabel("Y (Vehicle Y)")
plt.title("Feasible Region for Transport Cost Minimization")
plt.legend()
plt.grid()
plt.show()


c = [6, 7] 
A = [[3, 4], [2, 1]] 
b = [18, 10] 
bounds = [(0, None), (0, None)] 


result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
optimal_X, optimal_Y = result.x

optimal_X, optimal_Y, result.fun


# In[14]:


#No.8
x = np.linspace(0, 10, 400)  
y1 = (30 - 4 * x) / 3  
y2 = (18 - x) / 2  
y3 = (24 - 3 * x) / 2  

y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)
y3 = np.maximum(0, y3)


plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="4P1 + 3P2 <= 30")
plt.plot(x, y2, label="P1 + 2P2 <= 18")
plt.plot(x, y3, label="3P1 + 2P2 <= 24")
plt.fill_between(x, 0, np.minimum(np.minimum(y1, y2), y3), color="lightblue", alpha=0.5, label="Feasible Region")
plt.xlim(0, 10)
plt.ylim(0, 12)
plt.xlabel("P1 (Product 1)")
plt.ylabel("P2 (Product 2)")
plt.title("Feasible Region for Maximizing Revenue")
plt.legend()
plt.grid()
plt.show()


c = [-10, -12]
A = [[4, 3], [1, 2], [3, 2]]
b = [30, 18, 24] 
bounds = [(0, None), (0, None)]  


result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
optimal_P1, optimal_P2 = result.x

optimal_P1, optimal_P2, -result.fun


# In[15]:


#No.9
x = np.linspace(0, 4, 400)  
y1 = (5000 - 4000 * x) / 3000 
y2 = (4500 - 2000 * x) / 2500  
y3 = (3000 - 1000 * x) / 1500 


y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)
y3 = np.maximum(0, y3)


plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="4000A + 3000B <= 5000")
plt.plot(x, y2, label="2000A + 2500B <= 4500")
plt.plot(x, y3, label="1000A + 1500B <= 3000")
plt.fill_between(x, 0, np.minimum(np.minimum(y1, y2), y3), color="lightblue", alpha=0.5, label="Feasible Region")
plt.xlim(0, 4)
plt.ylim(0, 3)
plt.xlabel("A (Campaign A)")
plt.ylabel("B (Campaign B)")
plt.title("Feasible Region for Advertising Campaign Allocation")
plt.legend()
plt.grid()
plt.show()


c = [-500000, -400000]
A = [[4000, 3000], [2000, 2500], [1000, 1500]] 
b = [5000, 4500, 3000]  
bounds = [(0, None), (0, None)] 


result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
optimal_A, optimal_B = result.x

optimal_A, optimal_B, -result.fun


# In[16]:


#No.10
x = np.linspace(0, 20, 400)
y1 = (30 - 2 * x) / 4 
y2 = (24 - 3 * x) / 2 
y3 = (20 - x) / 2  


y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)
y3 = np.maximum(0, y3)


plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="2A + 4B <= 30")
plt.plot(x, y2, label="3A + 2B <= 24")
plt.plot(x, y3, label="A + 2B <= 20")
plt.fill_between(x, 0, np.minimum(np.minimum(y1, y2), y3), color="lightblue", alpha=0.5, label="Feasible Region")
plt.xlim(0, 15)
plt.ylim(0, 12)
plt.xlabel("A (Meal A)")
plt.ylabel("B (Meal B)")
plt.title("Feasible Region for School Cafeteria Meal Planning")
plt.legend()
plt.grid()
plt.show()


c = [-6, -5] 
A = [[2, 4], [3, 2], [1, 2]] 
b = [30, 24, 20] 
bounds = [(0, None), (0, None)]


result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
optimal_A, optimal_B = result.x

optimal_A, optimal_B, -result.fun


# In[ ]:




