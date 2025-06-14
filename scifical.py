# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import sympy as sp

# # Sci-Fi Themed Calculator Header
# st.title("🚀 Sci-Fi Calculator with Trigonometry Graphs")

# # User Input
# expression = st.text_input("Enter a mathematical expression (e.g., sin(x) + cos(x)):")

# if expression:
#     try:
#         # Convert input to a symbolic expression
#         x = sp.symbols('x')
#         parsed_expr = sp.sympify(expression)

#         # Display Computed Result
#         st.subheader("🛸 Computed Result:")
#         result = float(parsed_expr.subs(x, np.pi / 4))  # Convert to float
#         st.write(f"Expression evaluated at x = π/4: `{result}`")

#         # Generate Trigonometric Graph
#         st.subheader("🌌 Trigonometry Graph:")
#         x_vals = np.linspace(-2*np.pi, 2*np.pi, 400)

#         # Convert symbolic expression to numeric function
#         f_lambdified = sp.lambdify(x, parsed_expr, "numpy")
#         y_vals = np.array([f_lambdified(val) for val in x_vals])

#         # Plot
#         fig, ax = plt.subplots()
#         ax.plot(x_vals, y_vals, label=f"Graph of {expression}", color="cyan")
#         ax.set_xlabel("x")
#         ax.set_ylabel("f(x)")
#         ax.legend()
#         ax.grid()
#         st.pyplot(fig)

#     except Exception as e:
#         st.error(f"Error: {e}")

# # Sci-Fi Footer
# st.markdown("🌠 *Powered by Sci-Fi Math Algorithms!* 🌠")










import streamlit as st
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



st.set_page_config(page_title="🛸 Advanced Sci-Fi Calculator", page_icon="🧪")

# Styling for sci-fi aesthetics
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #0b0c10;
            color: #00f9ff;
            font-family: "Courier New", monospace;
        }
        .stButton>button {
            background-color: #1f2833;
            color: #66fcf1;
            border: 1px solid #45a29e;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Sci-Fi Calculator Console - Advanced Protocols")

st.sidebar.title("🧪 Select Calculation Mode")
mode = st.sidebar.radio("Choose an operation type", [
    "Arithmetic", "Trigonometry", "Logarithmic", "Matrix Operations", "Plot Trigonometric Graphs", "Plot Logarithmic Graphs"
])

# ========== 1. ARITHMETIC ==========
if mode == "Arithmetic":
    st.header("🔢 Arithmetic Engine")
    a = st.number_input("Enter Unit A")
    b = st.number_input("Enter Unit B")
    op = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide", "Power", "Modulus"])
    result = None
    if st.button("Execute"):
        try:
            if op == "Add":
                result = a + b
            elif op == "Subtract":
                result = a - b
            elif op == "Multiply":
                result = a * b
            elif op == "Divide":
                result = a / b if b != 0 else "Error: Divide by zero"
            elif op == "Power":
                result = math.pow(a, b)
            elif op == "Modulus":
                result = a % b
            st.success(f"🧮 Result: {result}")
        except Exception as e:
            st.error(f"Calculation error: {str(e)}")

# ========== 2. TRIGONOMETRY ==========
elif mode == "Trigonometry":
    st.header("📐 Trigonometric Reactor")
    angle = st.number_input("Input angle (degrees)", value=0.0)
    operation = st.selectbox("Choose function", ["sin", "cos", "tan", "asin", "acos", "atan"])
    result = None
    rad = math.radians(angle)
    if st.button("Compute"):
        try:
            if operation == "sin":
                result = math.sin(rad)
            elif operation == "cos":
                result = math.cos(rad)
            elif operation == "tan":
                result = math.tan(rad)
            elif operation == "asin":
                if -1 <= angle <= 1:
                    result = math.degrees(math.asin(angle))
                else:
                    result = "Error: Input must be in [-1, 1]"
            elif operation == "acos":
                if -1 <= angle <= 1:
                    result = math.degrees(math.acos(angle))
                else:
                    result = "Error: Input must be in [-1, 1]"
            elif operation == "atan":
                result = math.degrees(math.atan(angle))
            st.success(f"🧮 Result: {result}")
        except Exception as e:
            st.error(f"Calculation error: {str(e)}")

# ========== 3. LOGARITHMIC ==========
elif mode == "Logarithmic":
    st.header("📊 Logarithmic Computation")
    x = st.number_input("Input value (x>0 for log/ln)", value=1.0)
    op = st.selectbox("Choose function", ["log10", "ln", "exp"])
    result = None
    if st.button("Compute Log"):
        try:
            if op == "log10":
                if x > 0:
                    result = math.log10(x)
                else:
                    result = "Error: x must be > 0"
            elif op == "ln":
                if x > 0:
                    result = math.log(x)
                else:
                    result = "Error: x must be > 0"
            elif op == "exp":
                result = math.exp(x)
            st.success(f"🧮 Result: {result}")
        except Exception as e:
            st.error(f"Calculation error: {str(e)}")

# ========== 4. MATRIX OPERATIONS ==========
elif mode == "Matrix Operations":
    st.header("🧊 Matrix Core Protocol")
    matrix_input1 = st.text_area("Enter Matrix A (comma-separated rows)", "1,2\n3,4")
    matrix_input2 = st.text_area("Enter Matrix B (optional)", "5,6\n7,8")

    try:
        A = np.array([list(map(float, row.split(','))) for row in matrix_input1.strip().split('\n')])
        B = np.array([list(map(float, row.split(','))) for row in matrix_input2.strip().split('\n')])

        op = st.selectbox("Choose matrix operation", [
            "Add", "Subtract", "Multiply", "Transpose A", "Inverse A", "Determinant A"
        ])

        result = None
        if st.button("Execute Matrix Operation"):
            if op == "Add":
                result = A + B
            elif op == "Subtract":
                result = A - B
            elif op == "Multiply":
                result = A @ B
            elif op == "Transpose A":
                result = A.T
            elif op == "Inverse A":
                result = np.linalg.inv(A)
            elif op == "Determinant A":
                result = np.linalg.det(A)
            st.markdown("✅ **Result:**")
            st.write(result)
    except Exception as e:
        st.error(f"Matrix computation error: {str(e)}")

# ========== 5. TRIGONOMETRIC GRAPHS ==========
elif mode == "Plot Trigonometric Graphs":
    st.header("📈 Trigonometric Graph Reactor")
    function = st.selectbox("Choose trigonometric function", ["sin", "cos", "tan"])
    x_min = st.number_input("x-min (degrees)", -360)
    x_max = st.number_input("x-max (degrees)", 360)
    step = st.number_input("Step size", 1)

    if st.button("Plot Trig Graph"):
        try:
            x_vals = np.arange(x_min, x_max, step)
            x_rad = np.radians(x_vals)
            if function == "sin":
                y_vals = np.sin(x_rad)
            elif function == "cos":
                y_vals = np.cos(x_rad)
            elif function == "tan":
                y_vals = np.tan(x_rad)
                y_vals[np.abs(y_vals) > 10] = np.nan  # limit extreme tan values
            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals, color="#66fcf1")
            ax.set_title(f"{function}(x) Graph")
            ax.set_xlabel("Angle (degrees)")
            ax.set_ylabel("Value")
            ax.grid(True, color="#45a29e")
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Graph error: {str(e)}")

# ========== 6. LOGARITHMIC GRAPHS ==========
elif mode == "Plot Logarithmic Graphs":
    st.header("📈 Logarithmic Graph Reactor")
    function = st.selectbox("Choose function", ["log10", "ln", "exp"])
    x_min = st.number_input("x-min", 0.1)
    x_max = st.number_input("x-max", 10.0)
    step = st.number_input("Step size", 0.1)

    if st.button("Plot Log Graph"):
        try:
            x_vals = np.arange(x_min, x_max, step)
            if function == "log10":
                y_vals = np.log10(x_vals)
            elif function == "ln":
                y_vals = np.log(x_vals)
            elif function == "exp":
                y_vals = np.exp(x_vals)
            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals, color="#66fcf1")
            ax.set_title(f"{function}(x) Graph")
            ax.set_xlabel("x")
            ax.set_ylabel("Value")
            ax.grid(True, color="#45a29e")
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Graph error: {str(e)}")

# Footer
st.markdown("---")
st.caption("🛸 Powered by NumPy, Matplotlib, Streamlit, and Quantum Circuits v4.2")






# Upload data
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of Dataset")
    st.dataframe(df.head())

    st.subheader("Basic Statistics")
    st.write(df.describe())

    # Select columns for plotting
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    plot_type = st.selectbox("Select plot type", ["Histogram", "Line Chart", "Scatter Plot"])

    if plot_type == "Histogram":
        column = st.selectbox("Select column for histogram", numeric_columns)
        bins = st.slider("Number of bins", 5, 50, 20)
        fig, ax = plt.subplots()
        sns.histplot(df[column], bins=bins, kde=True, ax=ax)
        st.pyplot(fig)

    elif plot_type == "Line Chart":
        column = st.selectbox("Select column for line chart", numeric_columns)
        st.line_chart(df[column])

    elif plot_type == "Scatter Plot":
        col_x = st.selectbox("X-axis", numeric_columns)
        col_y = st.selectbox("Y-axis", numeric_columns)
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=col_x, y=col_y, ax=ax)
        st.pyplot(fig)
else:
    st.info("👈 Upload a CSV file to get started.")
