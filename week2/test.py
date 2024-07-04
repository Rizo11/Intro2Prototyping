import sympy as sp

# Define symbolic variables
q1, q2 = sp.symbols('q1 q2')
q = sp.Matrix([q1, q2])  # Joint positions vector
X = sp.Matrix([q1**2, q2**3])  # Example end-effector position function

# Compute Jacobian J(q)
J = X.jacobian(q)

# Compute time derivative dJ/dt
dq_dt = sp.Matrix([sp.diff(q1, 't'), sp.diff(q2, 't')])  # Joint velocities vector
dJ_dt = J.jacobian(q) @ dq_dt

# Print the time derivative of Jacobian
print("Time derivative of Jacobian:")
print(dJ_dt)