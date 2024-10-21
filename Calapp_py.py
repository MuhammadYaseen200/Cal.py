import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Simple Calculator Function
def simple_calculator():
    st.write("## Simple Calculator")
    operation = st.selectbox("Choose an operation", ["+", "-", "*", "/", "**", "sqrt"])

    if operation == "sqrt":
        num = st.number_input("Enter the number", value=0.0)
        if st.button("Calculate"):
            st.write(f"Result: {np.sqrt(num)}")
    else:
        num1 = st.number_input("Enter the first number", value=0.0)
        num2 = st.number_input("Enter the second number", value=0.0)
        if st.button("Calculate"):
            if operation == "+":
                st.write(f"Result: {num1 + num2}")
            elif operation == "-":
                st.write(f"Result: {num1 - num2}")
            elif operation == "*":
                st.write(f"Result: {num1 * num2}")
            elif operation == "/":
                if num2 != 0:
                    st.write(f"Result: {num1 / num2}")
                else:
                    st.write("Cannot divide by zero!")
            elif operation == "**":
                st.write(f"Result: {num1 ** num2}")

# Scientific Calculator Function
def scientific_calculator():
    st.write("## Scientific Calculator")
    operation = st.selectbox("Choose a function", ["sin", "cos", "tan", "exp", "log"])
    num = st.number_input("Enter the number", value=0.0)

    if st.button("Calculate"):
        if operation == "sin":
            st.write(f"Result: {np.sin(num)}")
        elif operation == "cos":
            st.write(f"Result: {np.cos(num)}")
        elif operation == "tan":
            st.write(f"Result: {np.tan(num)}")
        elif operation == "exp":
            st.write(f"Result: {np.exp(num)}")
        elif operation == "log":
            if num > 0:
                st.write(f"Result: {np.log(num)}")
            else:
                st.write("Logarithm undefined for non-positive numbers")

# Graphical Calculator Function
def plot_graph(x, y, title):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.axhline(0, color='black',linewidth=1)
    ax.axvline(0, color='black',linewidth=1)
    ax.set_title(title)
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.grid(True)
    st.pyplot(fig)

def graphical_calculator():
    st.write("## Graphical Calculator")
    graph_type = st.selectbox("Choose graph type", ["line", "parabola", "sine", "cosine"])
    x = np.linspace(-10, 10, 100)

    if graph_type == "line":
        m = st.number_input("Enter slope (m)", value=1.0)
        b = st.number_input("Enter intercept (b)", value=0.0)
        if st.button("Plot Line"):
            y = m * x + b
            plot_graph(x, y, f'y = {m}x + {b}')

    elif graph_type == "parabola":
        a = st.number_input("Enter coefficient a", value=1.0)
        b = st.number_input("Enter coefficient b", value=0.0)
        c = st.number_input("Enter constant c", value=0.0)
        if st.button("Plot Parabola"):
            y = a * x**2 + b * x + c
            plot_graph(x, y, f'y = {a}x² + {b}x + {c}')

    elif graph_type == "sine":
        if st.button("Plot Sine"):
            y = np.sin(x)
            plot_graph(x, y, 'y = sin(x)')

    elif graph_type == "cosine":
        if st.button("Plot Cosine"):
            y = np.cos(x)
            plot_graph(x, y, 'y = cos(x)')

# Streamlit App Main Function
def main():
    st.title("Scientific, Simple, and Graphical Calculator")

    # Sidebar for calculator options
    choice = st.sidebar.selectbox("Choose Calculator Type", ["Simple Calculator", "Scientific Calculator", "Graphical Calculator"])

    # Display corresponding calculator based on choice
    if choice == "Simple Calculator":
        simple_calculator()
    elif choice == "Scientific Calculator":
        scientific_calculator()
    elif choice == "Graphical Calculator":
        graphical_calculator()

if __name__ == '__main__':
    main()
              
