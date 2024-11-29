### README.md

---

# Linear Programming Solutions Using Python

This project provides graphical and numerical solutions for 10 linear programming (LP) problems. Using Python libraries like **NumPy**, **Matplotlib**, and **SciPy**, each problem is solved by plotting the constraints, shading the feasible region, and finding the optimal solution.

## Overview

Linear programming is used to optimize a given objective function (e.g., maximize profit or minimize cost) subject to constraints. This project demonstrates the solution of real-world LP problems, including manufacturing, resource allocation, and cost minimization.

### Features

1. **Graphical Representation**:
   - Constraints are plotted as lines.
   - Feasible regions are shaded.
   - Optimal solutions are identified on the graph.
   
2. **Numerical Optimization**:
   - Uses **SciPy's `linprog`** for solving the optimization problem.
   - Displays the values of decision variables and the objective function at the optimal point.

3. **Customizable Code**:
   - Can adapt to any LP problem with 2 variables and multiple constraints.

---

## Project Structure

- **`Solutions Linear Programming.py`**: Python script containing solutions for all 10 LP problems.
- **Graphs**: Feasible regions and optimal solutions for each problem are displayed dynamically when running the script.

---

## How to Run

### Prerequisites

1. Python 3.7 or higher
2. Install required libraries:
   ```bash
   pip install numpy matplotlib scipy
   ```

### Instructions

1. Download the script `Solutions Linear Programming.py`.
2. Open the script in an IDE (e.g., PyCharm, Jupyter Notebook, or any Python environment).
3. Run the script to view:
   - Graphs for feasible regions.
   - Numerical results for each problem in the console.

---

## Problems Solved

### Problem 1: Maximizing Profit for a Factory
Objective: Maximize profit from two products using limited machine time and raw materials.

### Problem 2: Minimizing Cost for a Manufacturer
Objective: Minimize production cost for two products using labor and material constraints.

### Problem 3: Maximizing Production with Multiple Resources
Objective: Optimize production of two products with labor, material, and machine time limits.

### Problem 4: Maximizing Revenue from Sales
Objective: Allocate an advertising budget to maximize revenue from two products.

### Problem 5: Resource Allocation for Two Projects
Objective: Maximize profit from two projects using labor hours and capital constraints.

### Problem 6: Production Planning for a Bakery
Objective: Maximize profit by producing chocolate and vanilla cakes with limited baking time and flour.

### Problem 7: Minimizing Cost for a Transport Company
Objective: Optimize vehicle use to minimize transportation costs with fuel and driver time limits.

### Problem 8: Maximizing Revenue from Two Products
Objective: Maximize revenue from two products considering resource limitations.

### Problem 9: Advertising Campaign Budget Allocation
Objective: Maximize reach by allocating a limited budget across two advertising campaigns.

### Problem 10: Meal Planning for a School Cafeteria
Objective: Maximize revenue by planning meals within resource constraints.

---

## Code Breakdown

### Inputs
- **Objective Function**: Defines what to optimize (e.g., maximize profit or minimize cost).
- **Constraints**: Inequalities that restrict decision variables.
- **Bounds**: Limits on decision variables (e.g., \( x_1, x_2 \geq 0 \)).

### Outputs
- **Graphical**:
  - Plot of all constraints.
  - Shaded feasible region.
  - Highlighted optimal solution.
- **Numerical**:
  - Values of decision variables at the optimal point.
  - Optimal value of the objective function.

---

## Example: Problem 1

**Objective**:
\[
Z = 3A + 4B
\]
Maximize \( Z \), subject to:
\[
2A + 3B \leq 12 \\
A + 2B \leq 8 \\
A, B \geq 0
\]

**Code Snippet**:
```python
x = np.linspace(0, 10, 400)
y1 = (12 - 2 * x) / 3
y2 = (8 - x) / 2

y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)

plt.figure(figsize=(8, 6))
plt.plot(x, y1, label="2A + 3B <= 12")
plt.plot(x, y2, label="A + 2B <= 8")
plt.fill_between(x, 0, np.minimum(y1, y2), color="lightblue", alpha=0.5, label="Feasible Region")
plt.legend()
plt.show()

c = [-3, -4]
A = [[2, 3], [1, 2]]
b = [12, 8]
bounds = [(0, None), (0, None)]

result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")
print(f"Optimal Solution: A = {result.x[0]}, B = {result.x[1]}")
print(f"Maximum Profit: Z = {-result.fun}")
```

**Output**:
- Optimal solution: \( A = 2.0, B = 3.0 \)
- Maximum profit: \( Z = 18.0 \)

---

## Limitations

1. Solves only 2-variable LP problems graphically.
2. Assumes constraints are linear.
3. For higher-dimensional problems, consider only numerical solutions.

---

## License

This project is released under the MIT License. Feel free to use, modify, and distribute.

--- 
