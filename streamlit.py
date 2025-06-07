import streamlit as st

# Streamlit app title
st.title("Simple Addition App")

# Input fields
num1 = st.number_input("Enter first number:", value=0)
num2 = st.number_input("Enter second number:", value=0)

# Calculate sum
sum_result = num1 + num2

# Display result
st.write(f"**Result:** {sum_result}")
