import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input numbers from the user
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

# Select operation
operation = st.selectbox("Choose the operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the selected operation
result = None
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")

# Display the result
if result is not None:
    st.success(f"The result is: {result}")
