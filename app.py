import streamlit as st
import numpy as np

# ==============================
# Helper: تحويل النص لدالة
# ==============================
def f(x, func_str):
    return eval(func_str)

# ==============================
# Bisection Method
# ==============================
def bisection(func_str, a, b, tol=1e-6, max_iter=100):
    if f(a, func_str) * f(b, func_str) >= 0:
        return "Invalid interval!"

    for i in range(max_iter):
        c = (a + b) / 2

        if abs(f(c, func_str)) < tol:
            return c

        if f(a, func_str) * f(c, func_str) < 0:
            b = c
        else:
            a = c

    return c


# ==============================
# Newton Method
# ==============================
def derivative(x, func_str, h=1e-6):
    return (f(x + h, func_str) - f(x - h, func_str)) / (2 * h)

def newton(func_str, x0, tol=1e-6, max_iter=100):
    x = x0

    for i in range(max_iter):
        d = derivative(x, func_str)

        if d == 0:
            return "Derivative = 0!"

        x_new = x - f(x, func_str) / d

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    return x


# ==============================
# Secant Method
# ==============================
def secant(func_str, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        if f(x1, func_str) - f(x0, func_str) == 0:
            return "Division by zero!"

        x2 = x1 - f(x1, func_str) * (x1 - x0) / (f(x1, func_str) - f(x0, func_str))

        if abs(x2 - x1) < tol:
            return x2

        x0, x1 = x1, x2

    return x2


# ==============================
# UI
# ==============================
st.title("📊 Numerical Methods Solver")

func = st.text_input("Enter Function (use x)", "x**3 - x - 2")

method = st.selectbox("Choose Method", ["Bisection", "Newton", "Secant"])

st.subheader("Inputs")

a = st.number_input("Enter a / x0", value=1.0)
b = st.number_input("Enter b / x1", value=2.0)

# ==============================
# Calculate
# ==============================
if st.button("Calculate"):
    try:
        if method == "Bisection":
            result = bisection(func, a, b)

        elif method == "Newton":
            result = newton(func, a)

        elif method == "Secant":
            result = secant(func, a, b)

        st.success(f"Result: {result}")

    except Exception as e:
        st.error(f"Error: {e}")


# ==============================
# Plot
# ==============================
st.subheader("📈 Function Plot")

x = np.linspace(a - 5, b + 5, 200)

try:
    y = [f(i, func) for i in x]

    st.line_chart(y)

except:
    st.warning("Cannot plot this function.")