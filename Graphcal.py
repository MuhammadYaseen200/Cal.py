# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Function for basic calculations
def basic_calculator():
    st.write("## Basic Calculator")

    operation = st.selectbox("Choose an operation", ["+", "-", "*", "/", "** (power)", "sqrt (square root)"])
    
    if operation == "sqrt":
        num = st.number_input("Enter number", value=0.0)
        if st.button("Calculate"):
            st.write(f"Result: {np.sqrt(num)}")
    else:
        num1 = st.number_input("Enter first number", value=0.0)
        num2 = st.number_input("Enter second number", value=0.0)
        if st.button("Calculate"):
            if operation == "+":
                st.write(f"Result: {num1 + num2}")
            elif operation == "-":
                st.write(f"Result: {num1 - num2}")
            elif operation == "*":
                st.write(f"Result: {num1 * num2}")
            elif operation == "/":
                st.write(f"Result: {num1 / num2}")
            elif operation == "** (power)":
                st.write(f"Result: {num1 ** num2}")

# Function for graphical calculations
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

# Helper function to plot the graph
def plot_graph(x, y, title):
    fig, ax = plt.subplots()
    ax.plot(x, y, label=title)
    ax.axhline(0, color='black',linewidth=1)
    ax.axvline(0, color='black',linewidth=1)
    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

# Streamlit app interface
def main():
    st.title("Scientific Calculator and Graph Plotter")

    # Menu for calculator types
    choice = st.sidebar.selectbox("Select Calculator Type", ["Basic Calculator", "Graphical Calculator"])

    # Show selected calculator
    if choice == "Basic Calculator":
        basic_calculator()
    elif choice == "Graphical Calculator":
        graphical_calculator()

# Run the Streamlit app
if __name__ == '__main__':
    main()
