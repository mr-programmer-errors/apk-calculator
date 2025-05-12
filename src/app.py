import streamlit as st
from utils.calculations import add, subtract, multiply, divide, power, square_root, logarithm, sine, cosine

st.title("APK Calculator")

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Inputs
num1 = st.number_input("Enter first number", key="num1")
num2 = st.number_input("Enter second number", key="num2")
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide", "Power", "Square Root (1st)", "Log (1st)", "Sin (1st)", "Cos (1st)"])

# Calculate
result = None
if operation == "Add":
    result = add(num1, num2)
elif operation == "Subtract":
    result = subtract(num1, num2)
elif operation == "Multiply":
    result = multiply(num1, num2)
elif operation == "Divide":
    result = divide(num1, num2)
elif operation == "Power":
    result = power(num1, num2)
elif operation == "Square Root (1st)":
    result = square_root(num1)
elif operation == "Log (1st)":
    result = logarithm(num1)
elif operation == "Sin (1st)":
    result = sine(num1)
elif operation == "Cos (1st)":
    result = cosine(num1)

# Show result
if result is not None:
    st.success(f"Result: {result}")
    st.session_state.history.append(f"{operation} → {result}")

# Show history
if st.session_state.history:
    st.subheader("History")
    for item in st.session_state.history[::-1]:
        st.write(item)

# Reset button
if st.button("Clear History"):
    st.session_state.history.clear()
    st.success("History cleared!")

# Footer
st.markdown(
    """
    <style>
    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)